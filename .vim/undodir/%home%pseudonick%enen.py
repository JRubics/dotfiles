Vim�UnDo� ����~ys<����R�����꼋�����   �                                   X�+    _�                             ����                                                                                                                                                                                                                                                                                                                                                             X�     �   	             %HERE%�                 �                3# Distributed under terms of the %LICENSE% license.�                %# Copyright © %YEAR% %USER% <%MAIL%>�              5�_�                   	        ����                                                                                                                                                                                                                                                                                                                                                             X�&     �      	          """5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             X�'     �      	           5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             X�'     �      	          """5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             X�*    �                  5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             X�"     �   	         �   #!/usr/bin/python       import platform, os, sys, pwd       """       ;Take an options dictionary and update /etc/veil/settings.py       """   def generateConfig(options):       !    config = """#!/usr/bin/python       b##################################################################################################   #   ## Veil-Framework configuration file   #   I# Run update.py to automatically set all these options to their defaults.   #   b##################################################################################################               1#################################################   #   # General system options   #   1#################################################       """   ,    print "\n Veil-Framework configuration:"       =    config += '# OS to use (Kali/Backtrack/Debian/Windows)\n'   J    config += 'OPERATING_SYSTEM="' + options['OPERATING_SYSTEM'] + '"\n\n'   D    print "\n [*] OPERATING_SYSTEM = " + options['OPERATING_SYSTEM']       O    config += '# Terminal clearing method to use (use "false" to disable it)\n'   F    config += 'TERMINAL_CLEAR="' + options['TERMINAL_CLEAR'] + '"\n\n'   >    print " [*] TERMINAL_CLEAR = " + options['TERMINAL_CLEAR']       $    config += '# Wine environment\n'   >    config += 'WINEPREFIX="' + options["WINEPREFIX"] + '"\n\n'   6    print " [*] WINEPREFIX = " + options["WINEPREFIX"]       /    config += '# Path to temporary directory\n'   :    config += 'TEMP_DIR="' + options["TEMP_DIR"] + '"\n\n'   2    print " [*] TEMP_DIR = " + options["TEMP_DIR"]       N    config += '# Default options to pass to msfvenom for shellcode creation\n'   J    config += 'MSFVENOM_OPTIONS="' + options['MSFVENOM_OPTIONS'] + '"\n\n'   B    print " [*] MSFVENOM_OPTIONS = " + options['MSFVENOM_OPTIONS']       g    config += '# The path to the metasploit framework, for example: /usr/share/metasploit-framework/\n'   H    config += 'METASPLOIT_PATH="' + options['METASPLOIT_PATH'] + '"\n\n'   @    print " [*] METASPLOIT_PATH = " + options['METASPLOIT_PATH']       J    config += '# The path to msfvenom for shellcode generation purposes\n'   D    config += 'MSFVENOM_PATH="' + options["MSFVENOM_PATH"] + '"\n\n'   <    print " [*] MSFVENOM_PATH = " + options["MSFVENOM_PATH"]       O    config += '# The path to pyinstaller, for example: /opt/pyinstaller-2.0/\n'   J    config += 'PYINSTALLER_PATH="' + options['PYINSTALLER_PATH'] + '"\n\n'   I    print " [*] PYINSTALLER_PATH = " + options['PYINSTALLER_PATH'] + "\n"               config += """   1#################################################   #   # Veil-Evasion specific options   #   1#################################################       """   -    config += '# Veil-Evasion install path\n'   L    config += 'VEIL_EVASION_PATH="' + options['VEIL_EVASION_PATH'] + '"\n\n'   D    print " [*] VEIL_EVASION_PATH = " + options['VEIL_EVASION_PATH']       D    source_path = os.path.expanduser(options["PAYLOAD_SOURCE_PATH"])   9    config += '# Path to output the source of payloads\n'   =    config += 'PAYLOAD_SOURCE_PATH="' + source_path + '"\n\n'   5    print " [*] PAYLOAD_SOURCE_PATH = " + source_path       7    # create the output source path if it doesn't exist   '    if not os.path.exists(source_path):            os.makedirs(source_path)   7        print " [*] Path '" + source_path + "' Created"       H    compiled_path = os.path.expanduser(options["PAYLOAD_COMPILED_PATH"])   4    config += '# Path to output compiled payloads\n'   @    config += 'PAYLOAD_COMPILED_PATH="' + compiled_path +'"\n\n'   9    print " [*] PAYLOAD_COMPILED_PATH = " + compiled_path       9    # create the output compiled path if it doesn't exist   +    if not os.path.exists( compiled_path ):   $        os.makedirs( compiled_path )   9        print " [*] Path '" + compiled_path + "' Created"       >    handler_path = os.path.expanduser(options["HANDLER_PATH"])   9    # create the output compiled path if it doesn't exist   *    if not os.path.exists( handler_path ):   #        os.makedirs( handler_path )   8        print " [*] Path '" + handler_path + "' Created"       R    config += '# Whether to generate a msf handler script and where to place it\n'   V    config += 'GENERATE_HANDLER_SCRIPT="' + options['GENERATE_HANDLER_SCRIPT'] + '"\n'   P    print " [*] GENERATE_HANDLER_SCRIPT = " + options['GENERATE_HANDLER_SCRIPT']   7    config += 'HANDLER_PATH="' + handler_path + '"\n\n'   /    print " [*] HANDLER_PATH = " + handler_path       8    hash_path = os.path.expanduser(options["HASH_LIST"])   ?    config += '# Running hash list of all payloads generated\n'   1    config += 'HASH_LIST="' + hash_path + '"\n\n'   0    print " [*] HASH_LIST = " + hash_path + "\n"               config += """   1#################################################   #    # Veil-Catapult specific options   #   1#################################################       """   .    config += '# Veil-Catapult install path\n'   N    config += 'VEIL_CATAPULT_PATH="' + options['VEIL_CATAPULT_PATH'] + '"\n\n'   F    print " [*] VEIL_CATAPULT_PATH = " + options['VEIL_CATAPULT_PATH']       R    catapult_resource_path = os.path.expanduser(options["CATAPULT_RESOURCE_PATH"])   ;    # create the catapult resource path if it doesn't exist   4    if not os.path.exists( catapult_resource_path ):   -        os.makedirs( catapult_resource_path )   B        print " [*] Path '" + catapult_resource_path + "' Created"   G    config += '# Path to output Veil-Catapult resource/cleanup files\n'   K    config += 'CATAPULT_RESOURCE_PATH="' + catapult_resource_path + '"\n\n'   J    print " [*] CATAPULT_RESOURCE_PATH = " + catapult_resource_path + "\n"           $    if platform.system() == "Linux":   =        # create the output compiled path if it doesn't exist   ,        if not os.path.exists("/etc/veil/"):   '            # os.makedirs("/etc/veil/")   .            os.system("sudo mkdir /etc/veil/")   9            os.system("sudo touch /etc/veil/settings.py")   =            os.system("sudo chmod 777 /etc/veil/settings.py")   2            print " [*] Path '/etc/veil/' Created"   .        f = open("/etc/veil/settings.py", 'w')           f.write(config)           f.close()   H        print " Configuration File Written To '/etc/veil/settings.py'\n"   	    else:   <        print " [!] ERROR: PLATFORM NOT CURRENTLY SUPPORTED"           sys.exit()           if __name__ == '__main__':           options = {}       $    if platform.system() == "Linux":       5        # check /etc/issue for the exact linux distro   )        issue = open("/etc/issue").read()       $        if issue.startswith("Kali"):   0            options["OPERATING_SYSTEM"] = "Kali"   /            options["TERMINAL_CLEAR"] = "clear"   K            options["METASPLOIT_PATH"] = "/usr/share/metasploit-framework/"   3            if os.path.isfile('/usr/bin/msfvenom'):   6                options["MSFVENOM_PATH"] = "/usr/bin/"               else:   c                msfpath = raw_input(" [>] Please enter the path of your metasploit installation: ")   2                options["MSFVENOM_PATH"] = msfpath   ;            if os.path.isdir('/opt/veil/PyInstaller-3.2/'):   J                options["PYINSTALLER_PATH"] = "/opt/veil/PyInstaller-3.2/"   9            elif os.path.isdir('/usr/share/pyinstaller'):   G                options["PYINSTALLER_PATH"] = '/usr/share/pyinstaller/'               else:   E                options["PYINSTALLER_PATH"] = "/opt/pyinstaller-2.0/"   +        elif issue.startswith("BackTrack"):   5            options["OPERATING_SYSTEM"] = "BackTrack"   /            options["TERMINAL_CLEAR"] = "clear"   @            options["METASPLOIT_PATH"] = "/opt/metasploit/msf3/"   3            if os.path.isfile('/usr/bin/msfvenom'):   6                options["MSFVENOM_PATH"] = "/usr/bin/"               else:   B                options["MSFVENOM_PATH"] = "/opt/metasploit/msf3/"   F            options["PYINSTALLER_PATH"] = "/opt/veil/PyInstaller-3.2/"           else:   1            options["OPERATING_SYSTEM"] = "Linux"   /            options["TERMINAL_CLEAR"] = "clear"   _            msfpath = raw_input(" [>] Please enter the path of your metasploit installation: ")   0            options["METASPLOIT_PATH"] = msfpath   3            if os.path.isfile('/usr/bin/msfvenom'):   6                options["MSFVENOM_PATH"] = "/usr/bin/"               else:   2                options["MSFVENOM_PATH"] = msfpath   F            options["PYINSTALLER_PATH"] = "/opt/veil/PyInstaller-3.2/"       %        # last of the general options   %        options["TEMP_DIR"] = "/tmp/"   (        options["MSFVENOM_OPTIONS"] = ""       9        # Get the real user if we're being ran under sudo           wineprefix = ""   M        user = os.environ.get("SUDO_USER", pwd.getpwuid(os.getuid()).pw_name)           if user == 'root':   3            wineprefix = "/root/.config/wine/veil/"           else:   @            wineprefix = "/home/" + user + "/.config/wine/veil/"   *        options["WINEPREFIX"] = wineprefix       '        # Veil-Evasion specific options   G        veil_evasion_path = "/".join(os.getcwd().split("/")[:-1]) + "/"   8        options["VEIL_EVASION_PATH"] = veil_evasion_path   I        options["PAYLOAD_SOURCE_PATH"] = "/usr/share/veil-output/source/"   M        options["PAYLOAD_COMPILED_PATH"] = "/usr/share/veil-output/compiled/"   3        options["GENERATE_HANDLER_SCRIPT"] = "True"   D        options["HANDLER_PATH"] = "/usr/share/veil-output/handlers/"   B        options["HASH_LIST"] = "/usr/share/veil-output/hashes.txt"       (        # Veil-Catapult specific options   V        veil_catapult_path = "/".join(os.getcwd().split("/")[:-2]) + "/Veil-Catapult/"   :        options["VEIL_CATAPULT_PATH"] = veil_catapult_path   N        options["CATAPULT_RESOURCE_PATH"] = "/usr/share/veil-output/catapult/"               # unsupported platform...   	    else:   <        print " [!] ERROR: PLATFORM NOT CURRENTLY SUPPORTED"           sys.exit()           generateConfig(options)        5��