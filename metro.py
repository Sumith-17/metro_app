import streamlit as st
import qrcode
import uuid
from io import BytesIO
from PIL import Image
from gtts import gTTS
import base64


def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit="True")
    img=qr.make_image(fill_color="black", back_color="white")
    return img

st.set_page_config(page_title="Metro Ticket Booking",page_icon="@")

st.title("METRO TICKET BOOKING SYSTEM WITH QR CODE")

stations=["AMeerpet","miyapur","lb nagar","kphb","jntu"]

name=st.text_input("Passenger Name")

source=st.selectbox("Source Station",stations)
destination=st.selectbox("Destination station",stations)

no_tickets=st.number_input("number of tickets",min_value=1,value=1)
price_per_ticket=30

total_amount=no_tickets * price_per_ticket

st.info(f"Total Amount :{total_amount}")

if st.button("book ticket"):
    if name.strip()=="":
        st.error("enter passenger name:")
    elif source==destination:
        st.error("same source and desti")
    else:
        booking_id=str(uuid.uuid4())[:8]

        qr_data=(
            f"booking id:{booking_id}\n"
            f"Name:{name}\n From: {source} \n To:{destination} \n Tickets:{no_tickets}"
            )
        qr_img=generate_qr(qr_data)

        buf= BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes=buf.getvalue()

        st.success("Ticket Booked Successfully:")

        st.write( "TICKET DETAILS")

        st.write(qr_data)
        st.write(f"AMount Paid : {total_amount}")
        st.image(qr_bytes,width=250)

        
            











