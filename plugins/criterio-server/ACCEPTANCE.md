# Acceptance criteria — criterio-server

Verified by `scripts/servidor.py --selftest` and `scripts/mapa.py --selftest`, on the PMO family alone and on the three families in one map.

## 1. The map

- [ ] Each agent is found by the folder of its configuration, `.criterio/<area>/[<instance>/]config.json`, and the state comes from that configuration; nothing is guessed.
- [ ] What the person leaves out is not served and does not come back on its own; a family installed later shows up as new.
- [ ] The map stores paths relative to the working folder.

## 2. It only serves what is written

- [ ] No page recomputes anything: the PMO report, each engine's reports, what falls due and the run history are served as the agents wrote them, with the date they were written.
- [ ] No file outside what it serves is reachable: paths with `..`, absolute paths, a state file that is not a report, an entry not on the map.

## 3. It writes no record

- [ ] The only file it writes is a request, in the `peticiones/` folder of the chosen agent's state, and the agent's record is byte for byte the same afterwards.
- [ ] A request for an agent that is not on the map is refused.

## 4. One portal

- [ ] The landing page leads to every agent of every family on the map, and the menu, the run history and the case pages include them.
- [ ] The agents come from `agentes.json`, written from the families by `scripts/familias.py`; the server names no agent by hand.

## 5. Access

- [ ] It listens on `127.0.0.1` unless told otherwise, and warns at startup when it listens beyond the machine. It authenticates nobody, and says so.
