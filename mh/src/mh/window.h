#pragma once

typedef struct GLFWwindow;

class __declspec(dllexport) window {
public:
	window();

private:
	GLFWwindow* m_window = nullptr;
};