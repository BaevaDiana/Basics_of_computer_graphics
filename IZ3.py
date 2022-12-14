from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Объявляем все глобальные переменные
global xrot         # Величина вращения по оси x
global yrot         # Величина вращения по оси y
global ambient      # рассеянное освещение
global treecolor    # Цвет ствола
global lightpos     # Положение источника освещения

def drawRectangle(x, y, z):
    step = 0.05
    glTranslatef(-x/2, -y/2, -z/2)
    i = 0
    j=0
    k=0
    while (abs(z-i) >= step/2):
        while (abs(j-y) >= step/2):
            while (abs(k-x) >= step/2):
                glutSolidCube(step)
                glTranslatef(step, 0, 0)
                k+=step
            k = 0
            glTranslatef(-x, 0, 0)
            glTranslatef(0, step, 0)
            j+=step
        j = 0
        glTranslatef(0, -y, 0)
        glTranslatef(0, 0, step)
        i+=step
    i = 0
    glTranslatef(0, 0, -z)

    glTranslatef(x/2, y/2, z/2)
  

def drawForest():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(-yrot, 0.0, 0, 1.0)  
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, treecolor)

    glTranslatef(1.3/2, 0.8/2, -0.5)
    drawRectangle(0.1, 0.1, 1.1)
    glTranslatef(-1.3/2, -0.8/2, 0.5)

    glTranslatef(-1.3/2, 0.8/2, -0.5)
    drawRectangle(0.1, 0.1, 1.1)
    glTranslatef(1.3/2, -0.8/2, 0.5)

    glTranslatef(1.3/2, -0.8/2, -0.5)
    drawRectangle(0.1, 0.1, 1.1)
    glTranslatef(-1.3/2, 0.8/2, 0.5)

    glTranslatef(-1.3/2, -0.8/2, -0.5)
    drawRectangle(0.1, 0.1, 1.1)
    glTranslatef(1.3/2, 0.8/2, 0.5)

    glTranslatef(-2.3/2, -1.8/2, -0.5)
    drawRectangle(0.1, 0.1, 1.1)
    glTranslatef(2.3/2, 1.8/2, 0.5)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.0, 100.0, 0.0))
    
    glTranslatef(1.3/2, 0.8/2, -0.2)                           # Сдвинемся по оси Z 
    # Рисуем нижние ветки (конус) с радиусом 0.5, высотой 0.5
    # Последние два числа определяют количество полигонов
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.4, 0.4, 20, 20)                             # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.3, 0.3, 20, 20)
    glTranslatef(-1.3/2, -0.8/2, 0.2)

    glTranslatef(-1.3/2, 0.8/2, -0.8)
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.4, 0.4, 20, 20)                             # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z
    glutSolidCone(0.3, 0.3, 20, 20)
    glTranslatef(1.3/2, -0.8/2, 0.5)

    glTranslatef(1.3/2, -0.8/2, -0.9)
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.4, 0.4, 20, 20)                             # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.3, 0.3, 20, 20)
    glTranslatef(-1.3/2, 0.8/2, 0.4)

    glTranslatef(-1.3/2, -0.8/2, -1.0)
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z на -0.3
    glutSolidCone(0.4, 0.4, 20, 20)                             # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z на -0.3
    glutSolidCone(0.3, 0.3, 20, 20)
    glTranslatef(1.3/2, 0.8/2, 0.5)

    glTranslatef(-2.3/2, -1.8/2, -1.2)
    glutSolidCone(0.5, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.4, 0.4, 20, 20)                             # Конус с радиусом 0.4, высотой 0.4
    glTranslatef(0.0, 0.0, 0.3)                                 # Сдвинемся по оси Z 
    glutSolidCone(0.3, 0.3, 20, 20)
    glTranslatef(2.3/2, 1.8/2, 0.5)

    glPopMatrix() 


# Процедура инициализации
def init():
    global xrot         # Величина вращения по оси x
    global yrot         # Величина вращения по оси y
    global ambient      # Рассеянное освещение
    global treecolor    # Цвет елочного ствола
    global lightpos     # Положение источника освещения

    xrot = 0.0                          # Величина вращения по оси x = 0
    yrot = 0.0                          # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 1)        # Первые три числа цвет в формате RGB, а последнее - яркость
    treecolor = (0.9, 0.6, 0.3, 0.8)    # Коричневый цвет для ствола
    lightpos = (2, -2, 0)          # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)                # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 1.0, 0.0, 0.0)                   # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Определяем положение источника света
    glEnable(GL_DEPTH_TEST)

# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot += 4.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot -= 4.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 4.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 4.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global treecolor

    #glClear(GL_COLOR_BUFFER_BIT) 
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    drawForest()  
    glutSwapBuffers()                                           # Выводим все нарисованное в памяти на экран

def mainDef(): 
    # Здесь начинается выполнение программы
    # Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # Указываем начальный размер окна (ширина, высота)
    glutInitWindowSize(600, 600)
    # Указываем начальное положение окна относительно левого верхнего угла экрана
    glutInitWindowPosition(50, 50)
    # Инициализация OpenGl
    glutInit(sys.argv)
    # Создаем окно с заголовком "Forest!"
    glutCreateWindow(b"Forest!")
    # Определяем процедуру, отвечающую за перерисовку
    glutDisplayFunc(draw)
    # Определяем процедуру, отвечающую за обработку клавиш
    glutSpecialFunc(specialkeys)
    # Вызываем нашу функцию инициализации
    init()
    # Запускаем основной цикл
    glutMainLoop()

mainDef()
