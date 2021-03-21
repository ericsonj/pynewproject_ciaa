import datetime
import os
from pathlib import Path
from pymakelib import nproject
from pkg_resources import resource_filename

class CIAA(nproject.BasicGenerator):
    """Generate basic c project for linux gcc
    """
    def info(self):
        return {
            "name": "CIAA Project",
            "desc": "Basic EDU-CIAA-NXP project"
        }


    def temp_files(self):
        return [
            'app/inc/app.h',
            'app/src/app.c',
            'app/app_mk.py',
            'makefile.mk',
            'Makefile',
            'Makefile.py',
            ".project",
            ".pymakeproj/.cproject_template",
            ".pymakeproj/.language.settings_template",
            ".settings",
            "scripts/config.py",
            "scripts/__init__py",
            "scripts/vscode_addon.py",
            "libs/arm_cortexM4lf_math_mk.py",
            "libs/firmware_v3_mk.py",
            ".gitignore"
        ]

    def get_attrs(self) -> dict:

        answers = [
            {
                "type": "input",
                "name": "project_name",
                "msg":  "Your project name: "
            },
            {   
                "type": "input",
                "name": "author",
                "msg":  "Your name: "
            },
            {
                "type": "input_path",
                "name": "firmware_path",
                "msg":  "Firmware_v3 path: "
            },
            {
                "type": "input_path",
                "name": "arm_none_eabi_path",
                "msg":  "Toolchain bin path: "
            }
        ]

        prompt = nproject.PromptUtil()

        prompt.add_answers(answers)
        obj = prompt.parse_answers()

        temp_tokens = {
            'date':         datetime.datetime.now().strftime("%b %d %Y"),
        }
        temp_tokens['project_name']         = obj.project_name
        temp_tokens['author']               = obj.author
        temp_tokens['firmware_path']        = obj.firmware_path
        temp_tokens['arm_none_eabi_path']   = obj.arm_none_eabi_path

        output_dir = Path( Path(os.getcwd()) / Path(obj.project_name)) 
        
        gzip_file = resource_filename("pynewproject_ciaa.templates", "ciaa_temp.tar.gz")

        return {
            "temp_name":        "ciaa_temp",
            "temp_gzip_file":   gzip_file,
            "temp_files":       self.temp_files(),
            "temp_tokens":      temp_tokens,
            "output_folder":    output_dir,
        }
