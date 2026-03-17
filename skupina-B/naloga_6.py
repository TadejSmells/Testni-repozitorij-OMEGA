minerals_info = [
    ("Quartz", "Colorless, but can be various colors", 7, "Vitreous", "Trigonal", "Jewelry, glass, electronics"),
    ("Feldspar", "Pink, white, gray", 6, "Vitreous", "Triclinic", "Ceramics, glass"),
    ("Mica", "Brown, colorless, green", 2.5, "Vitreous to pearly", "Monoclinic", "Insulation, cosmetics"),
    ("Calcite", "Colorless, white, yellow", 3, "Vitreous", "Trigonal", "Cement, lime production"),
    ("Dolomite", "White, gray", 3.5, "Vitreous to pearly", "Trigonal", "Construction, building materials"),
    ("Halite", "Colorless, white, blue", 2, "Vitreous", "Cubic", "Table salt"),
    ("Gypsum", "White, colorless", 2, "Vitreous to pearly", "Monoclinic", "Plaster, drywall"),
    ("Pyrite", "Brass-yellow", 6.5, "Metallic", "Isometric", "Sulfur production, jewelry"),
    ("Hematite", "Metallic gray or red", 5, "Metallic", "Trigonal", "Iron ore, pigments"),
    ("Magnetite", "Black", 5.5, "Metallic", "Isometric", "Iron ore, magnets"),
    ("Fluorite", "Colorless, purple, green", 4, "Vitreous", "Isometric", "Fluorine production, optics"),
    ("Talc", "White, greenish", 1, "Pearly", "Monoclinic", "Talcum powder, cosmetics"),
    ("Graphite", "Black", 1, "Metallic", "Hexagonal", "Pencils, lubricants"),
    ("Chalcopyrite", "Brass-yellow", 3.5, "Metallic", "Tetragonal", "Copper ore"),
    ("Apatite", "Green, yellow, blue", 5, "Vitreous", "Hexagonal", "Fertilizer, gemstones"),
    ("Cryolite", "White or colorless", 2.5, "Vitreous", "Cubic", "Aluminum production"),
    ("Bauxite", "Brown, red", 1, "Dull", "Amorphous", "Aluminum ore"),
    ("Barite", "Colorless, white", 3, "Vitreous", "Orthorhombic", "Drilling fluid, barium production"),
    ("Aragonite", "White, colorless", 3.5, "Vitreous to pearly", "Orthorhombic", "Calcium carbonate source"),
    ("Selenite", "Colorless, white", 2, "Vitreous to pearly", "Monoclinic", "Decorative stone")
]

for item in minerals_info:
    if item[2] > 5:
        print(f"Vaš mineral je {item[0]} in je {item[1]} barve. Lesk ima {item[3]} in je trši od povprečne trdote mineralov.")