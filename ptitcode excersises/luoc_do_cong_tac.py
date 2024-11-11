# Reimport the required library for diagram rendering
from graphviz import Digraph

# Create the collaboration diagram for the warranty process
collaboration_diagram = Digraph('Collaboration Diagram for Warranty Process', node_attr={'shape': 'box'}, format='png')

# Define the participants
collaboration_diagram.node('Customer', 'Customer (Khách hàng)')
collaboration_diagram.node('Manager', 'Service Center Manager (Trưởng trung tâm)')
collaboration_diagram.node('Technician', 'Service Technician (Nhân viên bảo hành)')
collaboration_diagram.node('Clerk', 'Warehouse Clerk (Thủ kho)')
collaboration_diagram.node('Warehouse', 'Warehouse (Kho)')
collaboration_diagram.node('Product', 'Product (Sản phẩm)')

# Define the interactions
collaboration_diagram.edge('Customer', 'Manager', label='Send product and warranty form')
collaboration_diagram.edge('Manager', 'Customer', label='Reject warranty or Accept warranty and assign')
collaboration_diagram.edge('Manager', 'Technician', label='Assign repair task')
collaboration_diagram.edge('Technician', 'Clerk', label='Request spare part')
collaboration_diagram.edge('Clerk', 'Warehouse', label='Check part availability')
collaboration_diagram.edge('Warehouse', 'Clerk', label='Provide part')
collaboration_diagram.edge('Clerk', 'Technician', label='Give spare part')
collaboration_diagram.edge('Technician', 'Product', label='Repair product')
collaboration_diagram.edge('Technician', 'Customer', label='Return repaired product and warranty form')

# Save and render the diagram
collaboration_diagram_output_path = '/mnt/data/collaboration_diagram_warranty'
collaboration_diagram.render(collaboration_diagram_output_path)

collaboration_diagram_output_path
