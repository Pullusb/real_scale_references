# Real scale references
Blender addon - Link references models at real world scale

**[Download latest](https://github.com/Pullusb/real_scale_references/archive/master.zip)**

### [Demo Youtube](https://youtu.be/-73m53QNolA)

Want to support me? [Check out this page](http://www.samuelbernou.fr/donate)

---  

## Description

Instant link some real world scale references for your modelisations.
Examples : humans, computer, pen etc...

The _Import references_ button create a new collection in which it link references models from a file.

![scale_ref_example](https://github.com/Pullusb/images_repo/raw/master/RSR_models_increasing.png)

Once you have finish using it, just click _Delete references_.

These models can be customized in the blend file located in the addon-folder > source (click on _open reference folder_ to access the file)
This blend file contains an addon-scripts (launch as autorun at open) that provide some tools to prepare your model.


### Where ?
Panel in sidebar : 3D view > sidebar 'N' > View > Real scale ref

### Why ?

When starting modelisation in blender we don't care much about making the model to scale.
Figuring out the real size needs some extra work (searching for approximate dimensions on the net, or measuring things IRL)

So often we skip this step (Proof : Extremely few models on BlendSwap are on scale... which is sad)
To make things worse, it's very difficult to appreciate the real size of the default cube alone in the scene (it's actually big, 2 meters high !)

But later it's very tedious when you want to combine multiple models in a new scene.
And rescaling can cause problem with some modifiers !

**The ideas is for you to have some visual _sensitive_ references to better fit your model in real world scale without worrying too much about numbers.**



### Note

I tried to add some generic usefull models, but if you made or found a CC0 model to scale that you think might be good to add in the references library send me a link or something (maybe open an issue to discuss it)

---


## Todo:
- make a demo
- add more reference models (some bigger model like building, car/truck and such)
- better tools to prepare model : delete material, check rotation, check scale factor etc...

### Ideas considered :
- Maybe hide the collection from the user to avoid mistake with renaming or moving (dont like of hiding things in data though...)
- Listing multiple blend folder (to allow multiple reference template), in this case list the collection name according to blend's name


---

## Changelog:
  v1.1.0 - 2019-11-25:
  - New option : Toggle X-ray (In front properties) on references
  - Fix : Linked collection don't become the active one
  - Fix : If objects or collection have been misplaced by the user in the 'scale_ref' folder, moved in a 'user_assets' collection.

  v1.0.0 - 2019-11-03:
  - New option to toggle visibility and lock object
