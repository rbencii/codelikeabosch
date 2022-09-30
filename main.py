from ui import UI

if __name__ == '__main__':
    try:
        UI = UI()
        while True:
            UI.update()
    except KeyboardInterrupt:
        print("Script terminated")