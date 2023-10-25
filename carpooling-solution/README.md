# PT_LT_Argos_Rafael_Castro
Prueba técnica Argos Rafael Castro

## Parte 1
Como parte de los proyectos de sostenibilidad de la compañía, se está buscando una solución que permita que los empleados publiquen sus rutas de transporte e indiquen los cupos que tienen disponibles en su vehículo, la hora de salida, el lugar de origen y el destino y que permita a los demás compañeros inscribirse en alguna de las rutas.

# Solución de Carpooling para la Sostenibilidad de la Compañía

## Tecnologías, lenguajes de programación y frameworks

### 1. **Frontend Web**:
- **Tecnología**: React
  - **Justificación**: React es un framework de JavaScript ampliamente usado y con amplia comunidad, facilita el desarrollo y mantenimiento de aplicaciones web complejas.

### 2. **Frontend Móvil**:
- **Tecnología**: React Native
  - **Justificación**: Con React Native, podemos desarrollar aplicaciones móviles nativas para Android e iOS con un único código base. Esto acelerará el proceso de desarrollo y reduce costos.

### 3. **Backend**:
- **Lenguaje**: Python
  - **Justificación**: Python es versátil y ampliamente adoptado, especialmente fuerte en integraciones y desarrollos web.
  
- **Framework**: FastAPI
  - **Justificación**: Flexible para construir APIs web, rápido y compatible con estandares como OpenAPI (documentación y testing).

### 4. **Autenticación y Autorización**:
- **Tecnología**: Amazon Cognito con integración a Directorio Activo mediante ADFS (Active Directory Federation Services)
  - **Justificación**: Amazon Cognito permite la federación de identidades con sistemas externos, incluido el Directorio Activo a través de ADFS, es robusta y escalable para autenticación y autorización.

### 5. **Base de datos**:
- **Tecnología**: PostgreSQL en Amazon RDS
  - **Justificación**: PostgreSQL es robusto y escalable. Al utilizar Amazon RDS, se facilita la gestión, la configuración, y la escalabilidad de la base de datos, beneficiándose de la infraestructura de AWS.

### 6. **Notificaciones**:
- **Tecnología**: Amazon SNS (Simple Notification Service)
  - **Justificación**: Amazon SNS es un servicio de AWS que permite enviar notificaciones a usuarios a través de diferentes formatos, incluidos SMS y correos electrónicos.

### 7. **Hosting y Despliegue**:
- **Tecnologías**:
  - **AWS Lambda**: Para ejecutar el código backend en respuesta a eventos, como solicitudes HTTP a través de API Gateway.
  - **Amazon API Gateway**: Para crear, publicar, mantener, monitorear y proteger las APIs REST a cualquier escala.
  - **Amazon S3**: Para almacenar y servir el frontend de la aplicación y otros recursos estáticos.
  - **Amazon CloudFront**: CDN para distribuir el contenido estáticamente alojado en S3 a nivel global y reducir latencias.
  - **Amazon Route 53**: Servicio de DNS para dirigir el tráfico web a los recursos adecuados, como CloudFront o API Gateway.
  - **Justificación**: La combinación de AWS Lambda con API Gateway permite una arquitectura serverless escalable y de bajo mantenimiento. S3 y CloudFront garantizan una entrega rápida y confiable del frontend y otros recursos estáticos. Route 53 proporciona una gestión confiable del DNS.
