# Rostrum on an organisation's server

[Español](rostrum-en-servidor.es.md)

Rostrum is the portal for every family: it publishes what the agents write for whoever will not open
a folder. To look at it for a while, `/criterio-server:server-start` on the user's computer is
enough. **This guide is for leaving it running**, with a stable link the sponsor opens tomorrow. It
is meant for whoever runs the server and whoever approves publishing it.

## What it needs, and what it does not

| Needs | Why |
|---|---|
| A computer on the internal network with Python 3.9 or later | Rostrum uses only Python's standard library: it installs no packages |
| That computer can see the agents' working folder | It reads the map and the state the agents leave. It writes in one place only: the `peticiones/` folder of the agent someone leaves a question for |
| A port | 8787 by default |
| Publishing it behind the access control the organisation already uses | **Rostrum does not authenticate, on purpose.** A server on the standard library will not authenticate better than the organisation's proxy |

**It does not need** a database, internet access, its own certificate, a privileged service account
or access to the language model (LLM): it runs no agent, it only serves what they already wrote.

## 1 · The map

The map says which agents it publishes and where their state is. `/criterio-server:server-setup`
writes it to `.criterio/rostrum/config.json`, inside the working folder, and its paths are
**relative to that folder**. So the server can mount the shared folder at any path: the only thing
that changes is the path given to `--mapa`.

## 2 · The code, at a path that does not change

Do not point at the installed plugin's code: its path changes with every version. Clone the
repository on the server, at the current version:

```
git clone --branch v2.2.0 https://github.com/josenanez/criterio /opt/criterio
```

To update, each time there is a new version —they are published on Fridays—:

```
cd /opt/criterio && git fetch --tags && git checkout v<version> && sudo systemctl restart rostrum
```

## 3 · Starting on its own

Rostrum listens on `127.0.0.1` and sits behind the proxy, which is what faces the network. In the
examples, the working folder is mounted at `/srv/criterio/trabajo`.

**Linux, with systemd** — `/etc/systemd/system/rostrum.service`:

```ini
[Unit]
Description=Rostrum, the Criterio portal
After=network-online.target remote-fs.target

[Service]
User=rostrum
ExecStart=/usr/bin/python3 /opt/criterio/plugins/criterio-server/scripts/servidor.py --mapa /srv/criterio/trabajo/.criterio/rostrum/config.json --puerto 8787
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl enable --now rostrum
```

The `rostrum` user needs to read the working folder and write to each agent's `peticiones/` folders,
and nothing else.

**macOS, with launchd** — `~/Library/LaunchAgents/com.criterio.rostrum.plist`, with the same
`ExecStart` line in `ProgramArguments`, and `RunAtLoad` and `KeepAlive` set to `true`; load it with
`launchctl load ~/Library/LaunchAgents/com.criterio.rostrum.plist`.

**Windows** — a Task Scheduler task that runs at startup:
`python.exe C:\criterio\plugins\criterio-server\scripts\servidor.py --mapa <map> --puerto 8787`.

`/criterio-server:server-start`, in a session on the server, builds the exact version of any of the
three with the real paths.

## 4 · Behind access control

Rostrum is published like any internal application. With nginx, the part that matters:

```nginx
location / {
    proxy_pass http://127.0.0.1:8787;
    proxy_set_header Host $host;
    # the authentication the organisation already uses goes here: SSO, LDAP or whatever it is
}
```

If the proxy is on another computer, Rostrum has to listen beyond its own: add `--abierto`, which
warns about it at startup, and let the firewall admit only the proxy.

## 5 · Checking it is right

```
curl -s http://127.0.0.1:8787/estado.json
```

It says how recent each agent's data is and how many open requests it has. If an agent shows no
state, it has not run yet: Rostrum invents nothing.

## Which link goes to whom

| Link | For whom |
|---|---|
| `/` | Everyone: the agents on the map and the form to leave them a question |
| `/resumen/<familia>` | The president and the committee: a family's executive summary on one printable page |
| `/vence` | Management: everything pending with a date, across every family |
| `/familia/<sigla>` | Whoever answers for that function |
| `/caso/<código>` | Whoever asks about a project, a product or a contract |

## What Rostrum does not do

It does not calculate or recalculate, writes no record, does not authenticate and sends nothing. A
question someone leaves in the form waits for its agent to run its clock
([decision 0028](decisions/0028-el-setup-ofrece-el-reloj.md)); the server cannot run an agent, and
that is deliberate.
