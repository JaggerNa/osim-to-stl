import opensim as osim
import vtk

def get_bone_geometry_file(model, bone_name):
    # get bone
    body = model.getBodySet().get(bone_name)
    geom = body.get_attached_geometry(0)
    mesh = osim.Mesh.safeDownCast(geom)
    mesh_file = mesh.get_mesh_file()

    return mesh_file

# load .osim file and init the file 
model = osim.Model('afterscale.osim')
state = model.initSystem()


mesh_file = get_bone_geometry_file(model, 'tibia_l') # this is an vtp file
print(mesh_file)


def convert_vtp_to_stl(input_vtp_file, output_stl_file):
    # read the input .vtp file
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(input_vtp_file)
    reader.Update()

    # write the output .stl file
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(output_stl_file)
    writer.SetInputConnection((reader.GetOutputPort()))
    writer.Write()


# Example
output_stl_file = './vtkout/yzx_tibia.stl'
convert_vtp_to_stl(mesh_file, output_stl_file)
