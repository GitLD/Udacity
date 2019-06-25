import time
import pyglet
import os
import webbrowser

def disp_start():
	""" Display Information when program start
	"""
	ct = time.ctime()
	print("Program Start at %s" % ct)

def disp_end():
	""" Display Information when program end
	"""
	ct = time.ctime()
	print("Program End at %s" % ct)

def run_app(path):
	player = pyglet.media.Player()
	source = pyglet.media.load(path)
	video_format = source.video_format
	window = pyglet.window.Window(width=video_format.width, height=video_format.height)
	
	player.queue(source)
	player.play()
	print(player.get_texture())
	
	@window.event
	def on_draw():
		window.clear()
		player.get_texture().blit(0, 0)
		
	pyglet.app.run()
	pyglet.app.exit()

def main():
	path = os.path.join(os.getcwd(),'media','aLIEz.mp4')
	url = 'https://music.163.com/#/video?id=969875A89904E2F4D88B672F62036D53&userid=1290932071'
	
	disp_start()
	break_times = 5
	break_count = 0
	
	
	while break_count < break_times:
		#run_app(path)
		webbrowser.open(url)
		time.sleep(30*60)
		break_count += 1

		
if __name__ == '__main__':
	main()