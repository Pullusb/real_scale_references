# Real scale references
Blender addon - Link references models at real world scale

**[Download latest](https://github.com/Pullusb/real_scale_references/archive/master.zip)**

<!-- ### [Demo Youtube](https://youtu.be/Rs4y7DeHkp8) -->

---  

## Why ?

When starting modelisation in blender we don't care much about making the model to scale.
Figuring out the real size needs some extra work (searching for approximate dimensions on the net, or measuring things IRL)

So often we skip this step (Proof : Extremely few models on BlendSwap are on scale... wich is sad)
To make thinks worse, it's very difficult to appreciate the real size of the default cube alone in the scene (it's actually big, 2 meters high !)

But later it's very tedious when you want to combine multiple models in a new scene.
And rescaling can cause problem with some modifiers !

**The ideas is for you to have some visual _sensitive_ references to better fit your model in real world scale without worrying too much about numbers.**

### Where ?
Panel in sidebar : 3D view > sidebar 'N' > View > Real scale ref


## Description

Instant link some real world scale references for your modelisations.
Exemples : humans, computer, pen etc...

The import button create a new collection in wich it link all the reference model from a file.
These models can be customized in the blend file located in the addon folder/source (to rea)
This blend file contains another addon (launch as autorun at open) that provide some tools to perpare your model.

Once you have finish, just click delete reference and voilà.

I tried to add some generic usefull models, but if you made or found a CC0 model to scale that you think might be good to add in the references library send me a link or something (maybe open an issue to discuss it)

---


## Todo:
- make a demo
- add more reference models (some bigger model like building, car/truck and such)


### Ideas considered :
- Maybe hide the collection from the user to avoid mistake with renaming or moving (dont like of hiding things in data though...)
- Listing multiple blend folder (to allow multiple template), in this case list the collection name accordingg to blend's name


---

## Changelog:

  v1.0.0 - 2019-11-03:
  - New option to toggle visibility and lock object
