from PyQt4 import QtCore,QtGui
import sys
import string
import ui
import sys, os,time


if __name__=='__main__':
	y_a=1.0
	y_b=1.0
	y_c=1.0
	y_d=1.0
	y_x=1.0
	def y_clean():
		a.lblB.setText('')
		a.lblD.setText('')
		a.leA.setText('')
		a.leC.setText('')
		a.pb_calculate.setEnabled(False)

	def y_calculate():
		if a.leA.displayText() == '' or a.leC.displayText()=='':
			return
		try:
			y_a=float(a.leA.displayText())
			y_c=float(a.leC.displayText())
		except:
			#a.pb_quit.click()
			return
		y_b=y_a-(y_a-y_c)/2
		y_d=y_c-(y_a-y_c)/2
		a.lblB.setNum(y_b)
		a.lblD.setNum(y_d)
		# set_pb_calculate_enable(False)
		# a.pb_calculate.setEnabled(False)
		print('ok')
	def set_pb_calculate_enable():
		a.pb_calculate.setEnabled(True)
	def set_tab_next():
		#a.focusNextPrevChild(True)
		a.leC.setFocus()


	app=QtGui.QApplication(sys.argv)
	a=ui.Ui_Dialog()
	#a.connect(a.btn1, QtCore.SIGNAL("clicked()"), mmsg)
	#a.btn_quit.clicked.connect(mQuit)
	a.pb_clean.clicked.connect(y_clean)
	a.leA.textEdited.connect(set_pb_calculate_enable)
	a.leC.textEdited.connect(set_pb_calculate_enable)
	a.pb_calculate.clicked.connect(y_calculate)
	# a.leC.editingFinished.connect(y_calculate)
	a.leA.editingFinished.connect(set_tab_next)
	#a.pb_clean.click()
	a.show();
	sys.exit(app.exec_())
