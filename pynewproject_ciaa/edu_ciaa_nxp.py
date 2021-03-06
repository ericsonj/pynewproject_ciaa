import datetime
import os
from pathlib import Path
from pymakelib import nproject
from pkg_resources import resource_filename

class EDU_CIAA_NXP(nproject.BasicGenerator):
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
            "scripts/ciaa_addon.py",
            "libs/arm_cortexM4lf_math_mk.py",
            "libs/firmware_v3_mk.py",
            ".gitignore",
            ".vscode/settings.json"
        ]

    def get_attrs(self, **kwargs) -> dict:

        args = self.parse_args(kwargs['args'])

        temp_tokens = {
            'date':         datetime.datetime.now().strftime("%b %d %Y"),
        }

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

        prompt_ans = []
        for a in answers:
            name = a['name']
            if name in args:
                temp_tokens[name] = args[name]
            else:
                prompt_ans.append(a)

        prompt = nproject.PromptUtil()

        prompt.add_answers(prompt_ans)
        obj = prompt.parse_answers()

        for a in answers:
            name = a['name']
            if hasattr(obj, name):
                temp_tokens[name] = getattr(obj, name)
        
        output_dir = Path( Path(os.getcwd()) / Path(temp_tokens['project_name'])) 
        
        gzip_file = resource_filename("pynewproject_ciaa.templates", "edu_ciaa_nxp.tar.gz")

        return {
            "temp_name":        "edu_ciaa_nxp",
            "temp_gzip_file":   gzip_file,
            "temp_files":       self.temp_files(),
            "temp_tokens":      temp_tokens,
            "output_folder":    output_dir,
        }
