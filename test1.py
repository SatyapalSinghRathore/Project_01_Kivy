from jnius import autoclass
from kivy.lang import Builder
from kivy.app import App

# def vibrate_phone():
#     PythonActivity = autoclass('org.kivy.android.PythonActivity')
#     Context = autoclass('android.content.Context')
#     vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)
#     vibrator.vibrate(1000)  # vibrate 1 sec

def vibrate_phone():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
    Build = autoclass('android.os.Build')
    VibrationEffect = autoclass('android.os.VibrationEffect')

    activity = PythonActivity.mActivity
    vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)

    if Build.VERSION.SDK_INT >= 26:
        effect = VibrationEffect.createOneShot(1000, VibrationEffect.DEFAULT_AMPLITUDE)
        vibrator.vibrate(effect)
    else:
        vibrator.vibrate(1000)

if __name__ == '__main__':
    kv = '''
BoxLayout:
    Button:
        text: 'Vibration'
        on_release: app.vibr()
    '''

    class Bluetooth(App):
        def build(self):
            return Builder.load_string(kv)

        def vibr(self):
            vibrate_phone()

            # pass

    Bluetooth().run()