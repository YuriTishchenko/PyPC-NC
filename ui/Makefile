PYFILES := MainWindow.py GraphicsView.py

all: $(PYFILES)

clean:
	rm -f $(PYFILES)

%.py: %.ui
# 	pyside-uic -o $@ $<
	/home/yuri/DEV/PyPC-NC/venv/bin/pyside2-uic -o $@ $<
