from mongoengine import connect


def establish_connection():
    connect('module8_2', host='mongodb+srv://denkuryshko:jGifeCXdc307DKl5@cluster0.fn0gjyt.mongodb.net/module8_2?retryWrites=true&w=majority&appName=Cluster0')
