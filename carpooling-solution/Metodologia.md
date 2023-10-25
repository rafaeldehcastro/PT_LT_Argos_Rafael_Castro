### Metodología de Desarrollo

Para abordar el desarrollo de la solución de carpooling para la sostenibilidad de la compañía, adoptaré la metodología **Agile**, específicamente **Scrum**, debido a su adaptabilidad, transparencia y capacidad para manejar cambios rápidos y frecuentes. Esta elección se basa en la necesidad de mantener a todas las partes interesadas informadas y de permitir la adaptabilidad a medida que descubrimos nuevos requisitos o cambios durante el desarrollo.

#### **1. Planificación Inicial**:
- Reuniré a todas las partes interesadas en una reunión de inicio para definir claramente los objetivos del proyecto, las expectativas y los entregables.
- Estableceré un Product Backlog inicial con todas las funcionalidades y requisitos identificados. Este backlog será dinámico y estará sujeto a cambios a lo largo del proyecto.

#### **2. Sprints**:
- Dividiré el desarrollo en sprints, que son períodos de tiempo definidos (por ejemplo, dos semanas), al final de los cuales se debe entregar un incremento del producto.
- Al comienzo de cada sprint, llevaré a cabo una reunión de planificación en la que seleccionaremos las tareas del Product Backlog que se abordarán durante ese sprint.
- Durante el sprint, el equipo trabajará en las tareas seleccionadas, y yo, como líder técnico, estaré disponible para resolver dudas, tomar decisiones técnicas y asegurar que el equipo siga las mejores prácticas.

#### **3. Reuniones Diarias (Daily Stand-ups)**:
- Organizaré breves reuniones diarias con el equipo de desarrollo para discutir el progreso, identificar obstáculos y asegurar que el sprint esté en el camino correcto.

#### **4. Revisiones de Sprint**:
- Al final de cada sprint, presentaré el incremento del producto a las partes interesadas para obtener su feedback.
- Este feedback será fundamental para adaptar y refinar el Product Backlog y garantizar que el producto final cumpla con las expectativas.

#### **5. Retrospectivas**:
- Después de cada revisión de sprint, llevaré a cabo una reunión de retrospectiva con el equipo de desarrollo. Esta reunión nos permitirá reflexionar sobre el sprint pasado, identificar áreas de mejora y discutir acciones para implementar esos cambios en el próximo sprint.

#### **6. Entrega y Despliegue Continuo**:
- Implementaré un proceso de integración y despliegue continuo (CI/CD) para asegurar que cada incremento del producto se pruebe y despliegue de manera eficiente en los entornos adecuados.

#### **7. Revisión Final y Entrega**:
- Una vez que todas las funcionalidades estén completas y probadas, organizaré una revisión final con todas las partes interesadas para demostrar el producto completo.
- A continuación, coordinaré el despliegue del producto en el entorno de producción y garantizaré que se entregue toda la documentación necesaria.

### Backlog del Producto
Teniendo en cuenta ésto y un escenario con 3 programadores más el líder técnico voy a presentar una primera aproximación a un backlog

#### **Épica 1: Autenticación y Autorización**

- **Historia de Usuario 1.1**: Como empleado, quiero poder autenticarme en la aplicación usando mis credenciales del Directorio Activo.
  - Tiempo Estimado: 3 días
  - Asignado a: Programador 1

- **Historia de Usuario 1.2**: Como líder técnico, quiero que la aplicación solo sea accesible para los usuarios de la compañía para garantizar la seguridad de la información.
  - Tiempo Estimado: 2 días
  - Asignado a: Programador 2

---

#### **Épica 2: Gestión de Rutas**

- **Historia de Usuario 2.1**: Como empleado, quiero poder registrar mi ruta de transporte para que otros empleados puedan verla y suscribirse a ella.
  - Tiempo Estimado: 4 días
  - Asignado a: Programador 1

- **Historia de Usuario 2.2**: Como empleado, quiero poder cancelar una ruta que he publicado.
  - Tiempo Estimado: 3 días
  - Asignado a: Programador 2

- **Historia de Usuario 2.3**: Como empleado, quiero ver las rutas disponibles para el día actual y poder suscribirme a ellas.
  - Tiempo Estimado: 4 días
  - Asignado a: Programador 3

---

#### **Épica 3: Notificaciones**

- **Historia de Usuario 3.1**: Como dueño de una ruta, quiero recibir notificaciones cuando alguien se suscribe o cancela su suscripción a mi ruta.
  - Tiempo Estimado: 3 días
  - Asignado a: Programador 3

- **Historia de Usuario 3.2**: Como empleado suscrito a una ruta, quiero recibir una notificación si la ruta es cancelada.
  - Tiempo Estimado: 2 días
  - Asignado a: Programador 1

---

#### **Épica 4: Interfaz de Usuario**

- **Historia de Usuario 4.1**: Como empleado, quiero una interfaz amigable y conforme al manual de marca de la compañía para interactuar con la aplicación.
  - Tiempo Estimado: 5 días
  - Asignado a: Programador 2 y Programador 3

---

#### **Épica 5: Despliegue e Integración**

- **Historia de Usuario 5.1**: Como líder técnico, quiero implementar CI/CD para asegurar una entrega y despliegue continuo.
  - Tiempo Estimado: 4 días
  - Asignado a: Líder Técnico

### Buenas Prácticas Metodológicas

Al implementar Scrum, como metodología Agile, se pueden garantizar entregas iterativas y obtener retroalimentación temprana. Las revisiones frecuentes y las retrospectivas aseguran la mejora continua. Además, usaré TDD (Test Driven Development) para asegurar la calidad del código desde el inicio, y CI/CD para una integración y despliegue continuos.

### Infraestructura y Plataformas

Se utilizará AWS debido a su robustez y versatilidad. Las principales tecnologías incluirán Lambda para funciones serverless, RDS con PostgreSQL para la base de datos, API Gateway para las APIs, y S3 junto con CloudFront para el frontend. Amazon Cognito facilitará la autenticación y autorización, además de Cloudwatch y X-ray para monitorización.

### Posibles Riesgos y Mitigación

1. **Cambios frecuentes en los requisitos**: La metodología Agile permite adaptarse a cambios. Sin embargo, es crucial definir claramente los requisitos desde el principio.
2. **Integración con Directorio Activo**: Podría haber desafíos técnicos al integrar con sistemas existentes. Es importante realizar pruebas tempranas y trabajar estrechamente con el equipo de IT para garantizar una integración sin problemas.
3. **Escalabilidad y performance**: Con un crecimiento en el número de usuarios, es vital que el sistema sea escalable. AWS Lambda y RDS proporcionan escalabilidad automática, pero se requiere monitoreo activo del rendimiento con las herramientas de AWS y de Git.

### Otros Elementos Necesarios

- **Documentación**: Es crucial tener una documentación detallada, tanto técnica como de usuario, para garantizar el correcto uso y mantenimiento del sistema.
- **Versionamiento**: Mantener versiones claramente definidas y documentadas del software es esencial. Usar herramientas como Git, en conjunción con plataformas como GitHub o GitLab, para gestionar el código fuente. Esto no sólo permite realizar un seguimiento de los cambios y colaborar eficientemente con el equipo sino también manetener un ambiente organizado y escalable para cambios de tecnologías móviles o web.
- **Formación**: Organizar sesiones de formación para los usuarios finales, asegurando que se sientan cómodos utilizando las nuevas plataformas.
- **Monitoreo y alertas**: Implementar herramientas de monitoreo y alerta para estar informado de cualquier problema en tiempo real y poder actuar rápidamente.
- **Rollback**: Revisar continuamente el performance implica también estar en la capacidad de reversar a versiones anteriores si se encuentran fallos.