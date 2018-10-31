inventory = {
    "Gold" : 500,
    "Pouch" : ["flint", "twine", "gemstone"],
    "Backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

inventory["Pocket"] = ['seashell', 'strange berry', 'lint']
inventory["Backpack"].remove("dagger")
inventory["Gold"] +=50