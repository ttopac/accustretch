assm_11_2_XY_fromAbaqSATfromSLDWRKSfromCreo works!!

It is difficult to export the sensor network to a proper .dxf file that Xiyuan's fab. software can read. Below are the steps we discovered that work:
1) Make sure stitch tolerance was very small (~1E-9) in the Abaqus assembly macro.
2) Export the assembly from Abaqus as Acis (.sat) format with R20 encoding.
3) Open this file in Solidworks (Used 2019/2020 student edition last time). It takes time. Save as .dxf there. Choose the view that has the network in full view (top view was the case for this example). Then it takes awfully long amount of time to process the design (~3 hours).
4) Finally edu version of Solidworks inserts a text at the bottom. We can use Creo to remove that: Open the .dxf file in Creo (5.0.4.0) and insert as drawing (default). Then remove the text, save with default options.
You can see if the generated .dxf will work using Layout Editor software (https://layouteditor.com/)