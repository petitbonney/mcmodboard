# mcmodboard

API and Web UI to manage modded Minecraft servers

## TODO

### Web UI

- Create a server
- Edit configuration

### API

- Run server from configuration
- Get server configurations

## Notes

- Modrinth API: https://docs.modrinth.com/#tag/projects
- Image: https://hub.docker.com/r/itzg/minecraft-server
- Docs: https://docker-minecraft-server.readthedocs.io/en/latest/
- Auto-download from Modrinth: https://docker-minecraft-server.readthedocs.io/en/latest/mods-and-plugins/modrinth/

### Configuration file template

```json
{
  "name": "My Super Server",
  "port": 25565,
  "minecraft_version": "1.21.1",
  "java_options": ["-Xms10G", "-Xmx10G", "-XX:+UseG1GC"],
  "loader": "fabric",
  "mods": {
    "fabric-api": "Ouxgt8PC",
    "sodium": "yaoBL9D9",
    "dungeons-and-taverns": "Bu5yOV7W"
  },
  "whitelist": ["notch", "petitbonney"],
  ""
}
```
