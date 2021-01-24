# ··· COLORS ···

black        = (0,0,0)
white        = (255,255,255)
red          = (255,0,0)
green        = (0,255,0)
blue         = (0,0,255)
yellow       = (255,255,0)
yellow_green = (154,205,50)
dark_olive   = (85,107,47)
green_yellow = (173,255,47)
grey         = (105,105,105)


# ··· SCREEN ···

size         = (1280, 720)
fps          = 60


# ··· POSITIONS ···

x = []
for i in range(10, 1250, 30):
	x.append(i)

y = []
for i in range(10, 700, 30):
	y.append(i)
print(x,y)


# ··· SETUP ···

point     = [0]

x_P       = 20
y_P       = 11

direccion = 'up'