import os
import sys
from time import sleep

try:
    import discord
    from dotenv import load_dotenv
    from colorama import init, Fore, Style, Back
except ModuleNotFoundError:
    print("You haven't installed the necessary modules")
    print("Please install them before running the script...", end="\n\n")
    print("Modules required (all):")
    print("    1. discord")
    print("    2. dotenv")
    print("    3. colorama", end="\n\n")
    print("Try the following command in the terminal/cmd (in current directory): ")
    print("      pip install -r requirements.txt ")
    print("              or ")
    print("      pip3 install -r requirements.txt ", end="\n\n")
    print("Closing the program...")
    sleep(2)
    exit()





def in_idle():
    try:
        return sys.stdin.__module__.startswith('idlelib')
    except AttributeError:
        return False


idle_nfo = in_idle()

if (idle_nfo == True):
    print("This program is not compatible with IDLE!!")
    print("Try running it in a terminal, shell or cmd", end="\n\n")
    print("Closing the program...")
    sleep(2)
    exit()


init(autoreset=True)

client = discord.Client()


bright_red = Fore.RED + Style.BRIGHT
bright_blue = Fore.BLUE + Style.BRIGHT
bright_cyan = Fore.CYAN + Style.BRIGHT
bright_yellow = Fore.YELLOW + Style.BRIGHT
bright_green = Fore.GREEN + Style.BRIGHT
white_bg = Back.WHITE
color_reset = Style.RESET_ALL

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def get_envInfo():
    key = ["", ""]
    value = ["", ""]
    s = 0
    fr = open(".env", "r")
    for line in fr.readlines():
        key[s], value[s] = line.split("=")
        key[s] = key[s].strip()
        value[s] = value[s].strip()
        s += 1
    fr.close()
    return key, value


def create_token(chan_id, token):
    key, value = get_envInfo()
        
    if (chan_id == "" and token == ""):
        print(bright_red + "Default bot token and channel ID are not set")
        print(bright_blue + "Please set them here ", end="\n\n")
        try:
            token = input(bright_cyan + "Enter bot token >> " + color_reset).strip()
        except KeyboardInterrupt:
            exit()
        p = 20
        while (p < 100):
            try:
                chan_id = int(input(bright_cyan + "Enter Main channel id >> " + color_reset))
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print(bright_red +  "Only Integer values", end="\n\n")
            else:
                f = open(".env", "w")
                f.write("DISCORD_TOKEN="+token+"\n")
                f.write("CHANNEL_ID="+str(chan_id)+"\n")
                f.close()
                return token, chan_id
                break
    elif (chan_id == ""):
        print(bright_red + "Default channel ID is not set")
        print(bright_blue + "Please enter a valid channel ID here", end="\n\n")
        p = 20
        while (p < 100):
            try:
                chan_id = int(input(bright_cyan + "Enter default channel id >> " + color_reset))
                
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print(bright_red + "Only Integer values", end="\n\n")
            else:
                f = open(".env", "w")
                f.write("DISCORD_TOKEN="+value[0]+"\n")
                f.write("CHANNEL_ID="+str(chan_id)+"\n")
                f.close()
                return value[0], chan_id
                break
    elif (token == ""):
        print(bright_red + "Default bot token is not set")
        print(bright_blue + "Please enter a valid bot token here", end="\n\n")
        try:
            token = input(bright_cyan + "Enter Bot token>> " + color_reset)
        except KeyboardInterrupt:
            exit()
        else:
            f = open(".env", "w")
            f.write("DISCORD_TOKEN="+token+"\n")
            f.write("CHANNEL_ID="+value[1]+"\n")
            f.close()
            return token, value[1]

def delete_token():
    key, value = get_envInfo()
    f = open(".env", "w")
    f.write("DISCORD_TOKEN=\n")
    f.write("CHANNEL_ID="+value[1]+"\n")
    f.close()

def delete_channel():
    key, value = get_envInfo()
    f = open(".env", "w")
    f.write("DISCORD_TOKEN="+value[0]+"\n")
    f.write("CHANNEL_ID=\n")
    f.close()

def chat_menu_help():
    print(" ", end="\n")
    print(bright_yellow + " Type /help for commands")
    print(bright_yellow + "Some basic commands:")
    print(bright_yellow + "       1. /prev  - Go back to previous menu")
    print(bright_yellow + "       2. /clean - Clear the window/terminal/console")
    print(bright_yellow + "       3. /quit  - exit the program")
    print(bright_yellow + "       4. /help  - print this help message", end="\n\n")


clear()

print(" ", end="\n")
print(bright_green + "A Simple                                   ")
print(bright_green + "  _______      _______    ____________     ")
print(bright_green + " |   __  |    |  ___  |  |____    ____|    ")
print(bright_green + " |  |__| |_   | |   | |       |  |         ")
print(bright_green + " |   __    |  | |   | |       |  |         ")
print(bright_green + " |  |__|   |  | |___| |       |  |         ")
print(bright_green + " |_________|  |_______|       |__|         ")
print(bright_green + "                                    Client ")
print(bright_red + "                           -By Mani        ", end="\n\n")


exitMsg = bright_red + "Press Ctrl + C to exit..."

k1 = 1
while (k1 < 2):
    if (os.path.exists(".env")):
        load_dotenv()
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN").strip()
        CHANNEL_ID = os.getenv("CHANNEL_ID").strip()
        k1 += 2
    else:
        f = open(".env", "w")
        f.write("DISCORD_TOKEN=\n")
        f.write("CHANNEL_ID=\n")
        f.close()



if (CHANNEL_ID == "" or DISCORD_TOKEN == ""):
    DISCORD_TOKEN, CHANNEL_ID = create_token(CHANNEL_ID, DISCORD_TOKEN)
    print(" ", end="\n")
    print(bright_green + "The bot token and channel ID have been successfully set")
else:
    print(bright_blue +"Default bot token and channel ID are already set")
    CHANNEL_ID = int(CHANNEL_ID)

    
print( "To add new default bot token and channel Id,")
print("you can delete the .env file and run program again", end="\n\n")
print(bright_red + "[NOTE: Refrain from editing the .env file]", end="\n\n")
print(bright_blue + "[UPDATE: Changing default channel ID and bot token are still under developement]", end="\n\n")
print(bright_blue + "New features will be added in the future!", end="\n\n")




@client.event
async def on_ready():
    global DISCORD_TOKEN
    global CHANNEL_ID
    print(bright_green +'We have logged in as {0.user}'.format(client), end="\n\n")
    i = 15
    n = 20
    while (n < 100):
        print(color_reset + "-"*100)
        print(bright_yellow + " >>>>>>>Welcome to discord bot client main menu<<<<<<<", end="\n\n")
        print("Choose your option (Type the number only)", end="\n\n")
        print(bright_green + "Options: ")
        print(bright_green + "   1. Chat in the default channel")
        print(bright_green + "   2. Chat in a different channel (Channel ID is required)")
        print(bright_green + "   3. Exit the program", end="\n\n")
        print(bright_green + "Enter either 1 / 2 / 3 only!!", end="\n\n")

        try:
            en_option = int(input(bright_cyan + "Choose option >> " + color_reset))
        except ValueError:
            print(" ", end="\n")
            print(bright_red + "An error occured, please try again", end="\n\n")
        else:
            if (en_option == 1):
                clear()
                print(bright_blue + "<<<<< Chat Box >>>>>>>>", end="\n\n")
                chat_menu_help()
                while (i < 100):
                    x = input(bright_cyan + "Enter message >> " + color_reset)
                    if (x == "/prev"):
                        clear()
                        break
                    elif (x == ""):
                        pass
                    elif (x == "/clean"):
                        clear()
                    elif (x == "/help"):
                        chat_menu_help()
                    elif (x == "/quit"):
                        clear()
                        print(exitMsg, end="\n\n")
                        return
                    else:
                        try:
                            await client.get_channel(CHANNEL_ID).send(x)
                            print(" ", end="\n")
                            print (bright_green + "Message has been sent!!", end="\n\n")
                        except discord.errors.HTTPException:
                            print(" ", end="\n")
                            print(bright_red + "You cannot send empty messages!", end="\n\n")
                        except AttributeError:
                            print(" ", end="\n")
                            print(bright_red + "An Error has occured!", end="\n\n")
                            print(Fore.BLACK + Style.BRIGHT + white_bg + "Possible Issues: ", end="\n\n")
                            print(bright_red + "1. Channel ID is Invalid")
                            print(bright_red + "2. Access restriction issues (Mainly for unix-like systems; eg:linux/Mac)" )
                            print(bright_red + "3. The .env file got tampered by someone")
                            print(bright_red + "3. Error in code[No quick fixes available]", end="\n\n")
                            print(bright_blue + "Identifying and fixing issues....", end="\n\n")
                            dots="."
                            for n2 in range(1, 7):
                                print('\r', bright_blue + white_bg + "Taking actions"+dots, end=" ", flush=True)
                                dots+="."
                                sleep(1)
                            delete_channel()
                            print(" ", end="\n\n")
                            print(bright_green + "Channel ID has been deleted")
                            print(bright_blue + "Re-run the program and enter a valid bot token", end="\n\n")
                            print(bright_yellow + "Other possible fixes(Attempt only if the above fix didn't work):", end="\n\n")
                            print(bright_blue + "a. Make sure necessary permissions are granted to work in the current directory")
                            print(bright_blue + "b. Try deleting the .env file and running the program again")
                            print(bright_blue + "c. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
                            print(exitMsg, end="\n\n")
                            return
            elif (en_option == 2):
                clear()
                print(bright_blue + " Switch to a different channel here (temporary)", end="\n\n")
                chat_menu_help()
                while (i < 200):
                    try:
                        drop_warn = False
                        temp_channel = input(bright_cyan + "Enter channel ID >> " + color_reset).strip()
                        if (temp_channel == "/prev"):
                            print(" ", end="\n")
                            print(bright_blue + "Going back to previous menu", end="\n\n")
                            break
                        elif (temp_channel == "/clean"):
                            drop_warn = True
                            clear()
                        elif (temp_channel == "/help"):
                            chat_menu_help()
                            continue
                        elif (temp_channel == "/quit"):
                            clear()
                            print(exitMsg, end="\n\n")
                            return
                        else:
                            temp_channel = int(temp_channel)
                    except ValueError:
                        print(" ", end="\n")
                        print(bright_red + "Only Integer type values", end="\n\n")
                    except:
                        print(" ", end="\n")
                        print(bright_red + "An unexpected error occured", end="\n\n")
                    else:
                        try:
                            if (drop_warn == True):
                                drop_warn = False
                                raise ValueError
                            else:
                                #try:
                                await client.get_channel(temp_channel).send(".")
                                #except ClientConnectorError:
                                    #print("Unable to connect, check your internet connection..")
                        except ValueError:
                            print(bright_blue + " Switch to a different channel here (temporary)", end="\n\n")
                        except:
                            print(" ", end="\n")
                            print(bright_red + "Cannot send message to this channel", end="\n\n")
                        else:
                            clear()
                            print(bright_yellow + "<<<<< Chat Box >>>>>>>>", end="\n\n")
                            chat_menu_help()
                            while (i < 100):
                                x = input(bright_cyan + "Enter message >> " + color_reset)
                                if (x == "/prev"):
                                    clear()
                                    print(bright_blue + " Switch to a different channel here (temporary)", end="\n\n")
                                    chat_menu_help()
                                    break
                                elif (x == ""):
                                    pass
                                elif (x == "/clean"):
                                    clear()
                                elif (x == "/help"):
                                    chat_menu_help()
                                elif (x == "/quit"):
                                    clear()
                                    print(exitMsg, end="\n\n")
                                    return
                                else:
                                    try:
                                        await client.get_channel(temp_channel).send(x)
                                    except discord.errors.HTTPException:
                                        print(" ", end="\n")
                                        print(bright_red + "You cannot send empty messages!", end="\n\n")
                                    else:
                                        print(" ", end="\n")
                                        print (bright_green + "Message has been sent!!", end="\n\n")
            elif (en_option == 3):
                clear()
                print(exitMsg, end="\n\n")
                break

            else:
                print(bright_red + "You have entered an invalid option. ")


try:
    client.run(DISCORD_TOKEN)
except discord.errors.LoginFailure:
    #login failure message
    print(" ", end="\n")
    print(bright_red + "An Error has occured!", end="\n\n")
    print(Fore.BLACK + Style.BRIGHT + white_bg + "Possible Issues: ", end="\n\n")
    print(bright_red + "1. Bot token is Invalid")
    print(bright_red + "2. Access restriction issues (Mainly for unix-like systems; eg:linux/Mac)" )
    print(bright_red + "3. The .env file got tampered by someone")
    print(bright_red + "3. Error in code[No quick fixes available]", end="\n\n")
    print(bright_red + "Identifying and fixing issues....", end="\n\n")
    dots="."
    for n1 in range(1, 7):
        print('\r', bright_blue + white_bg + "Taking actions"+dots, end=" ", flush=True)
        dots+="."
        sleep(1)
    delete_token()
    print(" ", end="\n\n")
    print(bright_green + "Bot token has been deleted")
    print(bright_blue + "Re-run the program and enter a valid bot token", end="\n\n")
    print(bright_yellow + "Other possible fixes(Attempt only if the above fix didn't work):", end="\n\n")
    print(bright_blue + "a. Make sure necessary permissions are granted to work in the current directory")
    print(bright_blue + "b. Try deleting the .env file and running the program again")
    print(bright_blue + "c. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
    
except:
    #any other issue message(mostly network connection based issues)
    print(" ")
    print(bright_red + "An Error has occured!", end="\n\n")
    print(Fore.BLACK + Style.BRIGHT + white_bg + "Possible Issues: ", end="\n\n")
    print(bright_red + "1. No/slow network connection")
    print(bright_red + "2. Required packages are not installed")
    print(bright_red + "3. Problems related to outdated software")
    print(bright_red + "4. The .env file got tampered by someone")
    print(bright_red + "5. Error in code[No quick fixes available]", end="\n\n")
    print(bright_yellow + "Fixes available: ", end="\n\n")
    print(bright_blue + "a. Reconnect to the network/Try connecting to a different network")
    print(bright_blue + "b. Make sure all the required packages are installed")
    print(bright_blue + "c. Make sure you aren't using an old version of python")
    print(bright_blue + "d. Try deleting the .env file and running the program again")
    print(bright_blue + "e. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
    
    
