from abaqusGui import getAFXApp
toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerKernelMenuButton(
    moduleName='switch_edges', functionName='switchEdges()',
    buttonText='Tools ME|Switch Edges Post',
    applicableModules=['Visualization'],
    version='1.0', author='Matthias Ernst',
    description='Plugin to quickly switch the visible edges in postprocessing.' \
    '\nThe plugin has nu UI. Each call will switch between Exterior and Feature edges.' \
    '\nWith the plugin it is now possible to use a custom toolbar and a custom button, that refers to the plugin. ' \
    'This allows now to make that switch by a click on that button. Go to Tools->Customize to create the toolbar and make the button assignment. '\
    'Ive simple reused the Mesh Region icon/button. You can also (or just) assign a shortcut to this plugin.'\
    '\nBe aware, that the button will be visible in all modules, but it will only work in the Visualization module.'
    '\n\nThis Plug-In is not an official Dassault Systemes product. Usage on your own risk.')