from helpers import helpers

def run(text):

    response = helpers.set_settings(text)
    helpers.generate_mp3_file(response)

if __name__ == '__main__':
    run()