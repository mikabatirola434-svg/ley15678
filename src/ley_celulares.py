
# ==========================================================
# Laboratorio de Programación (LPR 5° Año)
# E.E.S.T. N° 1 "Eduardo Ader" - Vicente López
# ACTIVIDAD 10: Simulador de Normativa de Celulares
# Ley 15.678
# DOCENTE: Yamil Gandulgia y Mansilla Muñoz York Elías
# ESTUDIANTE: Mikaela Batirola
# ==========================================================

print("==================================================")
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("==================================================\n")


autorizacion_docente = True
emergencia_familiar = True

print(f"Estado de Autorización Docente: {autorizacion_docente}")
print(f"Estado de Emergencia Validada: {emergencia_familiar}\n")


if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo para estudiar y aprender (Fines Pedagógicos).")

elif emergencia_familiar == True:
    print("[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente a través de preceptoría y/o dirección.")

else:
    print("[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("==================================================")
