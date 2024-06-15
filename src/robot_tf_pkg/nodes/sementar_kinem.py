import math

# Fungsi untuk menghitung sudut rotasi dan translasi
def calculate_omniwheel_motion(v1, v2, v3, d, time):
    # Konstanta untuk cosinus dan sinus dari sudut 120 dan 240 derajat
    cos_120 = -0.5
    sin_120 = math.sqrt(3) / 2
    cos_240 = -0.5
    sin_240 = -math.sqrt(3) / 2

    # Menghitung kecepatan translasi dalam sumbu x dan y
    Vx = (v1 + v2 * cos_120 + v3 * cos_240) / 3
    Vy = (v2 * sin_120 + v3 * sin_240) / 3

    # Menghitung kecepatan rotasi omega
    omega = (v1 + v2 + v3) / (3 * d)

    # Menghitung translasi pada sumbu x dan y selama waktu tertentu
    x_translation = Vx * time
    y_translation = Vy * time

    # Menghitung sudut rotasi selama waktu tertentu
    theta = omega * time

    return x_translation, y_translation, theta

# Parameter input
v1 = 0.0  # kecepatan roda 1 dalam meter
v2 = -1.0  # kecepatan roda 2 dalam meter
v3 = 1.0  # kecepatan roda 3 dalam meter
d = 0.3   # jarak dari pusat robot ke roda dalam meter
time = 1.0  # waktu dalam detik

# Menghitung hasil
x_translation, y_translation, theta = calculate_omniwheel_motion(v1, v2, v3, d, time)

# Menampilkan hasil
print(f"Translasi dalam sumbu x: {x_translation} meter")
print(f"Translasi dalam sumbu y: {y_translation} meter")
print(f"Sudut rotasi: {theta} radian")
