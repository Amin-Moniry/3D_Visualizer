import os

# Define the directory where your JavaScript libraries are stored
LIBS_DIR = "libs"

libs = {
    "THREE_UMD": "three.min.js",
    "GLTF_UMD": "GLTFLoader.js",
    "ORBIT_UMD": "OrbitControls.js",
}

# Read template file
with open("universal_template.html", encoding="utf-8") as f:
    html = f.read()

# Inline JavaScript injection
for key, filename in libs.items():
    # Construct the correct path to the file inside the new folder
    filepath = os.path.join(LIBS_DIR, filename)

    if os.path.exists(filepath):
        with open(filepath, encoding="utf-8") as f:
            html = html.replace(f"INJECT_{key}", f.read())
    else:
        print(f"[!] Warning: File {filepath} not found!")

# Save the final standalone file
with open("AminTivanix2_3D_Visualizer.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Standalone file AminTivanix2_3D_Visualizer.html successfully generated!")