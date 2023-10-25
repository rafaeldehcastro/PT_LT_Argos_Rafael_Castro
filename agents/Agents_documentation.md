## Documentación para `media_agents`

### Introducción

`media_agents` es un módulo que proporciona una serie de agentes (`AgentA`, `AgentB` y `AgentC`) diseñados para realizar cálculos específicos de media en listas de números y para generar patrones de escalera.

### Uso

1. **Importar el módulo**

    Primero, necesitas importar el módulo `media_agents`.

    ```python
    from media_agents import AgentFactory
    ```

2. **Crear un agente**

    Utiliza la fábrica `AgentFactory` para crear una instancia del agente que desees:

    ```python
    agent = AgentFactory.create_agent("A")  # Para el Agente A
    ```

    Puedes reemplazar "A" por "B" o "C" para otros agentes.

3. **Usar el agente**

    Una vez que tengas una instancia del agente, puedes llamar a sus métodos:

    - Para obtener la media:

        ```python
        result = agent.getMedia([1, 2, 3, 4, 5])
        ```

    - Para obtener la escalera:

        ```python
        staircase = agent.getStaircase(4)
        print(staircase)
        ```

### Pruebas

Para garantizar que `media_agents` funcione correctamente, se proporciona un conjunto de pruebas unitarias en `test_media_agents.py`.

**Ejecutar las pruebas**:

1. Abre una terminal.
2. Navega al directorio donde se encuentran `media_agents.py` y `test_media_agents.py`.
3. Ejecuta las pruebas con el siguiente comando:

    ```bash
    python -m unittest test_media_agents.py
    ```

Si todo está bien, deberías ver un mensaje indicando que todas las pruebas pasaron.

---

¡Eso es todo! Ahora deberías estar listo para usar `media_agents` y ejecutar las pruebas para verificar su correcto funcionamiento.