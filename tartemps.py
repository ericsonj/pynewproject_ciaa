import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

templates = [
    {
        "folder":  "pynewproject_ciaa/templates/edu_ciaa_nxp",
        "tarfile": "pynewproject_ciaa/templates/edu_ciaa_nxp.tar.gz"
    }
]

for temp in templates:
    print("Compress")
    if os.path.exists(temp['tarfile']):
        os.remove(temp['tarfile'])
    make_tarfile(temp['tarfile'], temp['folder'])