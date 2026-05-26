# ensayoEva3
Ensayo para evaluación de fundamentos de programación
Sistema de Control de Carga "Vuelo Chile" ✈️
¡Bienvenido a bordo! Este es un script interactivo en Python diseñado para automatizar, validar y agilizar el proceso de registro de equipajes para un vuelo. El programa actúa como un filtro inteligente en el mostrador del aeropuerto, asegurando que los datos sean correctos y clasificando la carga de forma automática para optimizar la seguridad del avión.

📋 Descripción del Proyecto
El programa permite registrar un número determinado de maletas ingresadas por el usuario. Para cada equipaje, se solicita un código de ticket y su peso en kilogramos, aplicando reglas estrictas de validación de datos en tiempo real. Al finalizar el proceso, genera un Manifiesto de Carga con el total de equipajes distribuidos entre la cabina y la bodega.

✨ Características Principales
Validación Robusta de Entradas: El sistema no se detiene ni falla si el usuario ingresa texto en lugar de números o valores negativos; gestiona los errores (ValueError) mediante bucles dinámicos.

Filtro de Seguridad para Tickets: Exige que los códigos de ticket tengan un formato válido (mínimo 5 caracteres y sin espacios intermedios).

Clasificación Automática de Carga: Aplica la regla aeronáutica del vuelo:

🧳 Equipaje de Cabina: Peso menor o igual a 10 kg.

📦 Equipaje de Bodega (Sobrecarga): Peso estricto mayor a 10 kg.

🚀 Requisitos y Ejecución
Requisitos Previos
Tener instalado Python 3.x en tu sistema.

Ejecución
Descarga o copia el archivo del código fuente (por ejemplo, control_carga.py).

Abre tu terminal o consola de comandos.

Ejecuta el script con el siguiente comando:

Bash
python control_carga.py
🛠️ ¿Cómo funciona el flujo de trabajo?
El script se ejecuta en 4 fases principales:

Definición del Lote: Se solicita la cantidad de maletas a procesar. No se permite continuar hasta que se ingrese un número entero positivo.

Control del Ticket: Se pide el código identificador. Si no cumple las reglas de longitud o contiene espacios, se vuelve a solicitar inmediatamente.

Pesaje Oficial: Se registra el peso de la maleta. Si ocurre un error de tipeo, el sistema insiste de forma segura sin perder el progreso del ticket actual.

Cierre de Manifiesto: Una vez alcanzado el total de equipajes, se imprimen los resultados consolidados.

📊 Ejemplo de Uso en Consola
Plaintext
Ingrese la cantidad de equipajes a registrar: 2

--- Registro del Equipaje N°1 ---
Ingrese Código de Ticket (mínimo 5 caracteres, sin espacios): AA123
Ingrese peso del equipaje AA123 (kg): 8
>> Ticket AA123: Clasificado como Equipaje de Cabina (Permitido).

--- Registro del Equipaje N°2 ---
Ingrese Código de Ticket (mínimo 5 caracteres, sin espacios): BB9876
Ingrese peso del equipaje BB9876 (kg): 15
>> Ticket BB9876: Clasificado como Equipaje de Bodega (Sobrecarga).

--------------------------------------------------
¡El avión transportará 1 equipajes en Cabina e 1 equipajes en Bodega!
¡Manifiesto de carga listo!
--------------------------------------------------
💡 Nota de desarrollo: Este programa está estructurado utilizando lógica limpia de control de flujo (while, try-except, continue y break), ideal para entornos educativos o consolas de comandos de misión crítica.
