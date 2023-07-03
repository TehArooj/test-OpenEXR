import imagecat
import graphcat.notebook
import logging
logging.basicConfig(level=logging.DEBUG)


mapping = {
    "CryptoPreview": {"role": imagecat.data.Role.RGB, "selection": ["R", "G", "B"]},
}

graph = graphcat.DynamicGraph()
imagecat.add_task(graph, "/load", imagecat.operator.load,
                  path="./Sample.exr")
imagecat.add_task(graph, "/preview", imagecat.operator.remap, mapping=mapping)
imagecat.add_links(graph, "/load", ("/preview", "image"))

graphcat.notebook.display(graph)
image = graph.output("/preview")

# imagecat.operator.save(graph, 'file_saver', [image,'./outputs','*'])

image.layers["CryptoPreview"]

graph.output("/load").metadata

# imagecat.add_task(graph, "/cryptomatte", imagecat.operator.cryptomatte.decoder,
#                   clown=False, mattes=["bunny_porcelain_mat"])
# imagecat.add_links(graph, "/load", ("/cryptomatte", "image"))

# graphcat.notebook.display(graph)
# image = graph.output("/cryptomatte")

# image.layers["M"]

# graph.set_task("/cryptomatte/mattes",
#                graphcat.constant(["flowerA_petal", "flowerB_petal"]))
# image = graph.output("/cryptomatte")

# image.layers["M"]


# graph.set_task("/cryptomatte/clown", graphcat.constant(True))
# graph.set_task("/cryptomatte/mattes", graphcat.constant(["bunny_porcelain_mat", "flowerA_petal",
#                "flowerB_petal", "flowerStem_mat", "grass_mat", "ground_mat", "smallLeaf_mat", "smallStalk_mat"]))
# image = graph.output("/cryptomatte")


# image.layers["M"]
