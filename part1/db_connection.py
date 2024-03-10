from mongoengine import connect


def establish_connection():
    connect('module8', host='mongodb+srv://denkuryshko:jGifeCXdc307DKl5@cluster0.fn0gjyt.mongodb.net/module8?retryWrites=true&w=majority&appName=Cluster0')
