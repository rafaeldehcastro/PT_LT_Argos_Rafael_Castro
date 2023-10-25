# PT_LT_Argos_Rafael_Castro
Prueba técnica Argos Rafael Castro

## Parte 1
Como parte de los proyectos de sostenibilidad de la compañía, se está buscando una solución que permita que los empleados publiquen sus rutas de transporte e indiquen los cupos que tienen disponibles en su vehículo, la hora de salida, el lugar de origen y el destino y que permita a los demás compañeros inscribirse en alguna de las rutas.

# Solución de Carpooling para la Sostenibilidad de la Compañía

## Tecnologías, lenguajes de programación y frameworks

### 1. **Frontend Web**:
- **Tecnología**: React
  - **Justificación**: React es un framework de JavaScript ampliamente usado y respaldado por una amplia comunidad. Su naturaleza componente-basada facilita el desarrollo y mantenimiento de aplicaciones web complejas.

### 2. **Frontend Móvil**:
- **Tecnología**: React Native
  - **Justificación**: Con React Native, podemos desarrollar aplicaciones móviles nativas para Android e iOS con un único código base. Esto acelera el proceso de desarrollo y reduce costos.

### 3. **Backend**:
- **Lenguaje**: Python
  - **Justificación**: Python es versátil y ampliamente adoptado, especialmente fuerte en integraciones y desarrollos web.
  
- **Framework**: Django y Django Rest Framework
  - **Justificación**: Django es un framework de alto nivel para desarrollo web que sigue el patrón modelo-vista-controlador. Django Rest Framework es una herramienta potente y flexible para construir APIs web. Ambos cuentan con una gran comunidad de apoyo.

### 4. **Autenticación y Autorización**:
- **Tecnología**: LDAP (Lightweight Directory Access Protocol)
  - **Justificación**: LDAP es adecuado para integrarse con directorios activos para autenticación y autorización.

### 5. **Base de datos**:
- **Tecnología**: PostgreSQL en Amazon RDS
  - **Justificación**: PostgreSQL es robusto y escalable. Al utilizar Amazon RDS, se facilita la gestión, la configuración, y la escalabilidad de la base de datos, beneficiándose de la infraestructura de AWS.

### 6. **Notificaciones**:
- **Tecnología**: Twilio (para notificaciones por SMS) y SendGrid (para notificaciones por correo electrónico)
  - **Justificación**: Ambas plataformas son líderes en sus campos y ofrecen soluciones robustas y fiables.

### 7. **Hosting y Despliegue**:
- **Tecnologías**:
  - **Amazon EC2**: Para alojar y ejecutar la aplicación backend y frontend web.
  - **Amazon S3**: Para almacenar y servir recursos estáticos y media.
  - **Amazon CloudFront**: CDN para distribuir el contenido a nivel global y reducir latencias.
  - **AWS Elastic Beanstalk**: Facilita el despliegue y escalado de aplicaciones.
  - **Justificación**: AWS ofrece una infraestructura robusta y escalable. EC2 y Elastic Beanstalk permiten un despliegue fácil y escalabilidad de la aplicación. S3 y CloudFront garantizan la entrega rápida y confiable de recursos.
