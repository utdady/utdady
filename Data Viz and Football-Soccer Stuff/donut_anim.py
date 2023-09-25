import imageio

with imageio.get_writer('donut_animation.gif', mode='I') as writer:
    for i in range(1,31):
        image = imageio.imread('donut'+ str(i)+ '.png')
        writer.append_data(image)
