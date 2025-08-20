bl_info = {
    "name": "Blender Session Timer",
    "author": "Hantaro",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Timer Tab",
    "description": "Shows how long Blender has been open",
    "category": "System"
}

import bpy, time

# Store start time
start_time = time.time()

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"

class TIMER_PT_panel(bpy.types.Panel):
    bl_label = "Session Timer"
    bl_idname = "TIMER_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Timer"

    def draw(self, context):
        layout = self.layout
        elapsed = time.time() - start_time
        layout.label(text=f"Time: {format_time(elapsed)}")

# Make the panel update every second
def redraw_timer():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()
    return 1.0  # run every 1 sec

def register():
    bpy.utils.register_class(TIMER_PT_panel)
    bpy.app.timers.register(redraw_timer)

def unregister():
    bpy.utils.unregister_class(TIMER_PT_panel)

if __name__ == "__main__":
    register()
