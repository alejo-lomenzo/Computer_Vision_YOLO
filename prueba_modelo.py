import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

# Cargar el modelo
@st.cache_resource
def load_model():
    return YOLO('C:/Users/Usuario/your_path/model_training/best.pt')

model = load_model()

def calcular_envido(cartas):
    palos = {'O': [], 'C': [], 'E': [], 'B': []}
    for carta in cartas:
        numero = int(carta[:-1])
        palo = carta[-1]
        if numero <= 7:
            palos[palo].append(numero)
        elif numero >= 10:
            palos[palo].append(0)  # Figuras valen 0 para el envido
    
    for palo, numeros in palos.items():
        if len(numeros) >= 2:
            numeros.sort(reverse=True)
            return sum(numeros[:2]) + 20
    
    return None  # No hay dos cartas del mismo palo

def process_image(image):
    results = model(image)
    cartas_detectadas = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            if conf > 0.5:  # Umbral de confianza
                nombre_clase = model.names[cls]
                cartas_detectadas.append(nombre_clase)
    
    valor_envido = calcular_envido(cartas_detectadas)
    
    return results[0].plot(), cartas_detectadas, valor_envido

def main():
    st.title("Detector de Envido - Truco Argentino")
    
    option = st.selectbox("Elige una opción", ["Subir imagen", "Probar en vivo"])
    
    if option == "Subir imagen":
        uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Imagen subida", use_column_width=True)
            if st.button("Procesar imagen"):
                processed_image, cartas, valor_envido = process_image(np.array(image))
                st.image(processed_image, caption="Imagen procesada", use_column_width=True)
                st.write(f"Cartas detectadas: {', '.join(cartas)}")
                if valor_envido:
                    st.success(f"¡Se puede cantar Envido! Valor: {valor_envido}")
                else:
                    st.warning("No se puede cantar Envido")
    
    elif option == "Probar en vivo":
        st.write("Cámara web en vivo")
        FRAME_WINDOW = st.image([])
        cap = cv2.VideoCapture(0)
        
        stop = st.button("Detener")
        
        while not stop:
            ret, frame = cap.read()
            if not ret:
                st.error("Error al capturar el frame")
                break
            
            processed_frame, cartas, valor_envido = process_image(frame)
            
            if valor_envido:
                cv2.putText(processed_frame, f"Envido: {valor_envido}", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(processed_frame, "No se puede cantar Envido", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            FRAME_WINDOW.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB))
            
        cap.release()

if __name__ == "__main__":
    main()