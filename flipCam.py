from maya import cmds

def flipCam():
	'''
	flips the camera
	'''
	
	flipGRP = 'mc_flip_cam_grp'
	
	if cmds.objExists(flipGRP):
		print(">> line 22 We got here!")
		cmds.setAttr(flipGRP+'.sx',(-1*cmds.getAttr(flipGRP+'.sx')))

	else:
		camList = []
		for item in cmds.ls(sl=True,type='transform'):
			if cmds.listRelatives(item,type='camera'):
				camList.append(cmds.listRelatives(item,type='camera')[0])
		if camList:
			camGrp = cmds.group(name='mc_flip_cam_grp',world=True,empty=True)
			cmds.parent(camList,camGrp,relative=True)
			cmds.setAttr(camGrp+'.sx',(-1*cmds.getAttr(camGrp+'.sx')))


if __name__ == '__main__':
	flipCam()