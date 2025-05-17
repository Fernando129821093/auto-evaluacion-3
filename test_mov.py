from SDK import ELITE
import numpy as np
import time

robot_ip = "169.168.0.200"  # ⚠️ Ajusta la IP del robot

robot = ELITE(robot_ip)

if robot.connect():
    print("✅ Conectado al robot")

    # Activar servos
    robot.set_servo_status(1)
    time.sleep(1)

    # Seleccionar sistema base y herramienta
    robot.set_user_number(0)
    robot.set_tool_number(0)

    # Definir pose destino en mm y grados: [x, y, z, rx, ry, rz]
    pose = np.array([0, 0, -60, 0, 0, 91])

    # Parámetros del movimiento lineal (MOVL)
    params = {
        "targetPose": pose.tolist(),
        "speed_type": 5,   # 0 = velocidad lineal en mm/s
        "speed": 5,      # velocidad mm/s
        "acc": 50,
        "dec": 50,
        "unit_type": 0,         # 0 = grados
        "coordinate_num": 0,    # 0 = base
        "tool_num": 0
    }

    print("▶ Enviando comando cmd_movel...")
    success, result, _ = robot.send_cmd("cmd_movel", params)

    if success:
        print("✅ Movimiento lineal ejecutado correctamente.")
        robot.wait_until_motion_complete()
    else:
        print("❌ Error en cmd_movel:", result)

    robot.disconnect()

else:
    print("❌ No se pudo conectar al robot.")
