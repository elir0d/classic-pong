import turtle
import winsound as ws

bounce = "D:\\Documentos\\DEVPROJECTS\\Python\\miniprojetos\\games\\classic-pong\\sound\\Pong_bounce.wav"
ball_l = "D:\\Documentos\\DEVPROJECTS\\Python\\miniprojetos\\games\\classic-pong\\sound\\paddle_l.wav"
ball_r = "D:\\Documentos\\DEVPROJECTS\\Python\\miniprojetos\\games\\classic-pong\\sound\\paddle_r.wav"

def play(s):
    if s == 0: ws.PlaySound(ball_l, ws.SND_ASYNC | ws.SND_FILENAME)
    if s == 1: ws.PlaySound(ball_r, ws.SND_ASYNC | ws.SND_FILENAME)
