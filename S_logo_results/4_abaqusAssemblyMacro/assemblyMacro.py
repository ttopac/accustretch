from abaqusConstants import *

session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/0.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P0', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P0'].Set(faces=mdb.models['Onerow_Stretch'].parts['P0'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P0'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P0'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/1.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P1', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P1'].Set(faces=mdb.models['Onerow_Stretch'].parts['P1'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P1'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P1'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/2.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P2', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P2'].Set(faces=mdb.models['Onerow_Stretch'].parts['P2'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P2'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P2'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/3.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P3', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P3'].Set(faces=mdb.models['Onerow_Stretch'].parts['P3'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P3'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P3'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/4.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P4', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P4'].Set(faces=mdb.models['Onerow_Stretch'].parts['P4'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P4'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P4'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/5.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P5', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P5'].Set(faces=mdb.models['Onerow_Stretch'].parts['P5'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P5'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P5'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/6.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P6', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P6'].Set(faces=mdb.models['Onerow_Stretch'].parts['P6'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P6'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P6'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/7.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P7', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P7'].Set(faces=mdb.models['Onerow_Stretch'].parts['P7'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P7'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P7'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/8.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P8', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P8'].Set(faces=mdb.models['Onerow_Stretch'].parts['P8'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P8'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P8'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/9.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P9', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P9'].Set(faces=mdb.models['Onerow_Stretch'].parts['P9'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P9'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P9'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/10.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P10', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P10'].Set(faces=mdb.models['Onerow_Stretch'].parts['P10'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P10'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P10'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/11.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P11', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P11'].Set(faces=mdb.models['Onerow_Stretch'].parts['P11'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P11'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P11'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/12.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P12', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P12'].Set(faces=mdb.models['Onerow_Stretch'].parts['P12'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P12'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P12'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/13.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P13', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P13'].Set(faces=mdb.models['Onerow_Stretch'].parts['P13'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P13'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P13'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/14.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P14', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P14'].Set(faces=mdb.models['Onerow_Stretch'].parts['P14'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P14'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P14'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/15.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P15', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P15'].Set(faces=mdb.models['Onerow_Stretch'].parts['P15'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P15'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P15'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/16.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P16', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P16'].Set(faces=mdb.models['Onerow_Stretch'].parts['P16'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P16'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P16'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/17.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P17', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P17'].Set(faces=mdb.models['Onerow_Stretch'].parts['P17'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P17'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P17'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/18.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P18', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P18'].Set(faces=mdb.models['Onerow_Stretch'].parts['P18'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P18'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P18'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/19.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P19', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P19'].Set(faces=mdb.models['Onerow_Stretch'].parts['P19'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P19'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P19'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/20.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P20', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P20'].Set(faces=mdb.models['Onerow_Stretch'].parts['P20'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P20'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P20'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/21.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P21', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P21'].Set(faces=mdb.models['Onerow_Stretch'].parts['P21'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P21'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P21'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/22.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P22', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P22'].Set(faces=mdb.models['Onerow_Stretch'].parts['P22'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P22'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P22'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/23.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P23', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P23'].Set(faces=mdb.models['Onerow_Stretch'].parts['P23'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P23'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P23'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/24.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P24', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P24'].Set(faces=mdb.models['Onerow_Stretch'].parts['P24'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P24'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P24'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/25.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P25', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P25'].Set(faces=mdb.models['Onerow_Stretch'].parts['P25'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P25'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P25'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/26.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P26', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P26'].Set(faces=mdb.models['Onerow_Stretch'].parts['P26'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P26'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P26'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/27.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P27', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P27'].Set(faces=mdb.models['Onerow_Stretch'].parts['P27'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P27'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P27'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/28.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P28', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P28'].Set(faces=mdb.models['Onerow_Stretch'].parts['P28'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P28'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P28'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/29.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P29', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P29'].Set(faces=mdb.models['Onerow_Stretch'].parts['P29'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P29'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P29'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/30.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P30', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P30'].Set(faces=mdb.models['Onerow_Stretch'].parts['P30'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P30'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P30'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/31.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P31', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P31'].Set(faces=mdb.models['Onerow_Stretch'].parts['P31'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P31'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P31'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/32.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P32', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P32'].Set(faces=mdb.models['Onerow_Stretch'].parts['P32'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P32'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P32'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/33.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P33', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P33'].Set(faces=mdb.models['Onerow_Stretch'].parts['P33'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P33'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P33'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/34.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P34', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P34'].Set(faces=mdb.models['Onerow_Stretch'].parts['P34'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P34'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P34'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/35.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P35', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P35'].Set(faces=mdb.models['Onerow_Stretch'].parts['P35'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P35'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P35'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/36.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P36', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P36'].Set(faces=mdb.models['Onerow_Stretch'].parts['P36'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P36'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P36'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/37.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P37', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P37'].Set(faces=mdb.models['Onerow_Stretch'].parts['P37'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P37'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P37'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/38.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P38', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P38'].Set(faces=mdb.models['Onerow_Stretch'].parts['P38'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P38'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P38'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/39.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P39', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P39'].Set(faces=mdb.models['Onerow_Stretch'].parts['P39'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P39'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P39'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/40.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P40', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P40'].Set(faces=mdb.models['Onerow_Stretch'].parts['P40'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P40'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P40'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/41.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P41', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P41'].Set(faces=mdb.models['Onerow_Stretch'].parts['P41'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P41'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P41'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/42.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P42', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P42'].Set(faces=mdb.models['Onerow_Stretch'].parts['P42'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P42'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P42'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/43.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P43', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P43'].Set(faces=mdb.models['Onerow_Stretch'].parts['P43'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P43'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P43'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/44.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P44', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P44'].Set(faces=mdb.models['Onerow_Stretch'].parts['P44'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P44'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P44'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/45.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P45', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P45'].Set(faces=mdb.models['Onerow_Stretch'].parts['P45'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P45'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P45'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/46.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P46', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P46'].Set(faces=mdb.models['Onerow_Stretch'].parts['P46'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P46'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P46'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/47.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P47', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P47'].Set(faces=mdb.models['Onerow_Stretch'].parts['P47'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P47'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P47'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/48.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P48', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P48'].Set(faces=mdb.models['Onerow_Stretch'].parts['P48'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P48'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P48'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/49.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P49', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P49'].Set(faces=mdb.models['Onerow_Stretch'].parts['P49'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P49'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P49'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/50.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P50', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P50'].Set(faces=mdb.models['Onerow_Stretch'].parts['P50'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P50'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P50'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/51.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P51', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P51'].Set(faces=mdb.models['Onerow_Stretch'].parts['P51'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P51'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P51'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/52.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P52', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P52'].Set(faces=mdb.models['Onerow_Stretch'].parts['P52'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P52'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P52'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/53.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P53', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P53'].Set(faces=mdb.models['Onerow_Stretch'].parts['P53'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P53'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P53'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/54.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P54', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P54'].Set(faces=mdb.models['Onerow_Stretch'].parts['P54'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P54'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P54'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/55.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P55', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P55'].Set(faces=mdb.models['Onerow_Stretch'].parts['P55'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P55'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P55'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/56.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P56', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P56'].Set(faces=mdb.models['Onerow_Stretch'].parts['P56'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P56'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P56'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/57.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P57', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P57'].Set(faces=mdb.models['Onerow_Stretch'].parts['P57'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P57'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P57'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/58.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P58', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P58'].Set(faces=mdb.models['Onerow_Stretch'].parts['P58'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P58'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P58'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/59.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P59', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P59'].Set(faces=mdb.models['Onerow_Stretch'].parts['P59'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P59'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P59'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/60.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P60', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P60'].Set(faces=mdb.models['Onerow_Stretch'].parts['P60'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P60'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P60'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/61.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P61', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P61'].Set(faces=mdb.models['Onerow_Stretch'].parts['P61'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P61'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P61'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/62.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P62', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P62'].Set(faces=mdb.models['Onerow_Stretch'].parts['P62'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P62'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P62'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/63.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P63', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P63'].Set(faces=mdb.models['Onerow_Stretch'].parts['P63'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P63'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P63'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/64.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P64', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P64'].Set(faces=mdb.models['Onerow_Stretch'].parts['P64'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P64'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P64'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/65.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P65', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P65'].Set(faces=mdb.models['Onerow_Stretch'].parts['P65'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P65'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P65'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/66.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P66', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P66'].Set(faces=mdb.models['Onerow_Stretch'].parts['P66'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P66'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P66'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/67.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P67', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P67'].Set(faces=mdb.models['Onerow_Stretch'].parts['P67'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P67'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P67'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/68.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P68', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P68'].Set(faces=mdb.models['Onerow_Stretch'].parts['P68'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P68'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P68'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/69.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P69', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P69'].Set(faces=mdb.models['Onerow_Stretch'].parts['P69'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P69'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P69'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/70.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P70', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P70'].Set(faces=mdb.models['Onerow_Stretch'].parts['P70'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P70'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P70'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/71.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P71', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P71'].Set(faces=mdb.models['Onerow_Stretch'].parts['P71'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P71'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P71'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/72.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P72', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P72'].Set(faces=mdb.models['Onerow_Stretch'].parts['P72'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P72'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P72'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/73.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P73', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P73'].Set(faces=mdb.models['Onerow_Stretch'].parts['P73'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P73'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P73'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/74.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P74', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P74'].Set(faces=mdb.models['Onerow_Stretch'].parts['P74'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P74'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P74'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/75.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P75', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P75'].Set(faces=mdb.models['Onerow_Stretch'].parts['P75'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P75'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P75'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/76.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P76', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P76'].Set(faces=mdb.models['Onerow_Stretch'].parts['P76'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P76'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P76'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/77.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P77', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P77'].Set(faces=mdb.models['Onerow_Stretch'].parts['P77'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P77'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P77'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/78.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P78', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P78'].Set(faces=mdb.models['Onerow_Stretch'].parts['P78'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P78'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P78'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/79.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P79', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P79'].Set(faces=mdb.models['Onerow_Stretch'].parts['P79'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P79'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P79'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/80.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P80', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P80'].Set(faces=mdb.models['Onerow_Stretch'].parts['P80'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P80'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P80'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/81.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P81', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P81'].Set(faces=mdb.models['Onerow_Stretch'].parts['P81'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P81'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P81'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/82.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P82', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P82'].Set(faces=mdb.models['Onerow_Stretch'].parts['P82'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P82'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P82'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/83.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P83', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P83'].Set(faces=mdb.models['Onerow_Stretch'].parts['P83'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P83'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P83'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/84.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P84', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P84'].Set(faces=mdb.models['Onerow_Stretch'].parts['P84'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P84'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P84'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/85.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P85', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P85'].Set(faces=mdb.models['Onerow_Stretch'].parts['P85'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P85'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P85'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/86.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P86', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P86'].Set(faces=mdb.models['Onerow_Stretch'].parts['P86'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P86'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P86'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/87.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P87', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P87'].Set(faces=mdb.models['Onerow_Stretch'].parts['P87'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P87'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P87'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/88.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P88', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P88'].Set(faces=mdb.models['Onerow_Stretch'].parts['P88'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P88'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P88'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/89.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P89', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P89'].Set(faces=mdb.models['Onerow_Stretch'].parts['P89'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P89'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P89'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/90.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P90', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P90'].Set(faces=mdb.models['Onerow_Stretch'].parts['P90'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P90'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P90'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/91.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P91', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P91'].Set(faces=mdb.models['Onerow_Stretch'].parts['P91'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P91'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P91'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/92.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P92', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P92'].Set(faces=mdb.models['Onerow_Stretch'].parts['P92'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P92'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P92'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/93.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P93', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P93'].Set(faces=mdb.models['Onerow_Stretch'].parts['P93'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P93'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P93'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/94.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P94', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P94'].Set(faces=mdb.models['Onerow_Stretch'].parts['P94'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P94'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P94'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/95.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P95', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P95'].Set(faces=mdb.models['Onerow_Stretch'].parts['P95'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P95'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P95'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/96.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P96', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P96'].Set(faces=mdb.models['Onerow_Stretch'].parts['P96'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P96'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P96'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/97.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P97', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P97'].Set(faces=mdb.models['Onerow_Stretch'].parts['P97'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P97'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P97'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/98.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P98', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P98'].Set(faces=mdb.models['Onerow_Stretch'].parts['P98'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P98'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P98'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/99.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P99', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P99'].Set(faces=mdb.models['Onerow_Stretch'].parts['P99'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P99'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P99'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/100.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P100', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P100'].Set(faces=mdb.models['Onerow_Stretch'].parts['P100'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P100'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P100'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/101.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P101', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P101'].Set(faces=mdb.models['Onerow_Stretch'].parts['P101'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P101'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P101'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/102.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P102', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P102'].Set(faces=mdb.models['Onerow_Stretch'].parts['P102'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P102'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P102'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/103.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P103', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P103'].Set(faces=mdb.models['Onerow_Stretch'].parts['P103'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P103'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P103'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/104.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P104', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P104'].Set(faces=mdb.models['Onerow_Stretch'].parts['P104'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P104'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P104'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/105.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P105', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P105'].Set(faces=mdb.models['Onerow_Stretch'].parts['P105'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P105'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P105'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/106.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P106', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P106'].Set(faces=mdb.models['Onerow_Stretch'].parts['P106'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P106'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P106'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/107.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P107', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P107'].Set(faces=mdb.models['Onerow_Stretch'].parts['P107'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P107'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P107'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/108.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P108', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P108'].Set(faces=mdb.models['Onerow_Stretch'].parts['P108'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P108'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P108'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(referenceRepresentation=ON)
step = mdb.openStep('C:/Users/Tanay/OneDrive - Leland Stanford Junior University/Research_Personal/Mar19_HemisphereDip/7.2_OptimusAbaqusOpt/6_generateAbaqusAssembly/designFiles/109.stp', scaleFromFile=OFF)
mdb.models['Onerow_Stretch'].PartFromGeometryFile(name='P109', geometryFile=step, combine=True, mergeSolidRegions=True, stitchTolerance=0.001, dimensionality=THREE_D, type=DEFORMABLE_BODY)
mdb.models['Onerow_Stretch'].parts['P109'].Set(faces=mdb.models['Onerow_Stretch'].parts['P109'].faces.getSequenceFromMask(('[#ffffffff:5 ]', ), ), name='Set-20')
mdb.models['Onerow_Stretch'].parts['P109'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=mdb.models['Onerow_Stretch'].parts['P109'].sets['Set-20'], sectionName='Sand_Sec', thicknessAssignment=FROM_SECTION)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-0', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-0', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-0', ), vector=(1.2, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-1', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-1', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-1', ), vector=(5.512000025087255, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-2', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-2', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-2', ), vector=(10.059958005881164, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-3', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-3', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-3', ), vector=(14.508804768921076, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-4', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-4', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-4', ), vector=(19.012862412528825, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-5', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-5', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-5', ), vector=(23.32486243237677, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-6', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-6', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-6', ), vector=(27.80722285609002, 0.028, 1.2))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-7', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-7', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-7', ), vector=(1.2, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-8', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-8', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-8', ), vector=(5.512000025087255, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-9', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-9', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-9', ), vector=(10.059958005881164, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-10', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-10', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-10', ), vector=(14.508804768921076, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-11', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-11', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-11', ), vector=(19.012862412528825, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-12', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-12', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-12', ), vector=(23.32486243237677, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-13', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-13', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-13', ), vector=(27.80722285609002, 0.028, 5.609843525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-14', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-14', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-14', ), vector=(1.2, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-15', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-15', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-15', ), vector=(5.512000025087255, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-16', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-16', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-16', ), vector=(10.059958005881164, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-17', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-17', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-17', ), vector=(14.508804768921076, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-18', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-18', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-18', ), vector=(19.012862412528825, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-19', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-19', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-19', ), vector=(23.32486243237677, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-20', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-20', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-20', ), vector=(27.80722285609002, 0.028, 10.042115177501584))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-21', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-21', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-21', ), vector=(1.2, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-22', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-22', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-22', ), vector=(5.512000025087255, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-23', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-23', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-23', ), vector=(10.059958005881164, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-24', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-24', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-24', ), vector=(14.508804768921076, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-25', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-25', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-25', ), vector=(19.012862412528825, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-26', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-26', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-26', ), vector=(23.32486243237677, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-27', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-27', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-27', ), vector=(27.80722285609002, 0.028, 14.465403289391581))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-28', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-28', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-28', ), vector=(1.2, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-29', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-29', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-29', ), vector=(5.512000025087255, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-30', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-30', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-30', ), vector=(10.059958005881164, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-31', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-31', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-31', ), vector=(14.508804768921076, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-32', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-32', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-32', ), vector=(19.012862412528825, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-33', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-33', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-33', ), vector=(23.32486243237677, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-34', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-34', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-34', ), vector=(27.80722285609002, 0.028, 19.01370757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-35', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-35', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-35', ), vector=(1.2, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-36', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-36', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-36', ), vector=(5.512000025087255, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-37', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-37', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-37', ), vector=(10.059958005881164, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-38', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-38', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-38', ), vector=(14.508804768921076, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-39', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-39', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-39', ), vector=(19.012862412528825, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-40', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-40', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-40', ), vector=(23.32486243237677, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-41', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-41', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-41', ), vector=(27.80722285609002, 0.028, 23.325707573658953))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-42', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-42', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-42', ), vector=(1.2, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-43', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-43', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-43', ), vector=(5.512000025087255, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-44', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-44', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-44', ), vector=(10.059958005881164, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-45', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-45', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-45', ), vector=(14.508804768921076, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-46', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-46', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-46', ), vector=(19.012862412528825, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-47', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-47', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-47', ), vector=(23.32486243237677, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-48', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-48', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-48', ), vector=(27.80722285609002, 0.028, 27.78494336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-49', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-49', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-49', ), vector=(1.2, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-50', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-50', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-50', ), vector=(5.512000025087255, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-51', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-51', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-51', ), vector=(10.059958005881164, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-52', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-52', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-52', ), vector=(14.508804768921076, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-53', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-53', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-53', ), vector=(19.012862412528825, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-54', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-54', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-54', ), vector=(23.32486243237677, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-55', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-55', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-55', ), vector=(27.80722285609002, 0.028, 32.17874832900493))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-56', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-56', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-56', ), vector=(1.2, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-57', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-57', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-57', ), vector=(5.512000025087255, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-58', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-58', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-58', ), vector=(10.059958005881164, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-59', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-59', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-59', ), vector=(14.508804768921076, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-60', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-60', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-60', ), vector=(19.012862412528825, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-61', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-61', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-61', ), vector=(23.32486243237677, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['NodeOnly']
a.Instance(name='NodeOnly-62', part=p, dependent=ON)
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('NodeOnly-62', ), axisPoint=(0.0, 0.0, 0.0), axisDirection=(1.0, 0.0, 0.0), angle=90.0)
a.translate(instanceList=('NodeOnly-62', ), vector=(27.80722285609002, 0.028, 36.49568964593179))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P0']
a.Instance(name='P0-0', part=p, dependent=ON)
a.translate(instanceList=('P0-0', ), vector=(2.456, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P1']
a.Instance(name='P1-0', part=p, dependent=ON)
a.translate(instanceList=('P1-0', ), vector=(6.768000025087256, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P2']
a.Instance(name='P2-0', part=p, dependent=ON)
a.translate(instanceList=('P2-0', ), vector=(11.315958005881164, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P3']
a.Instance(name='P3-0', part=p, dependent=ON)
a.translate(instanceList=('P3-0', ), vector=(15.764804768921076, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P4']
a.Instance(name='P4-0', part=p, dependent=ON)
a.translate(instanceList=('P4-0', ), vector=(20.268862412528826, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P5']
a.Instance(name='P5-0', part=p, dependent=ON)
a.translate(instanceList=('P5-0', ), vector=(24.58086243237677, 0, -0.1867))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P6']
a.Instance(name='P6-0', part=p, dependent=ON)
a.translate(instanceList=('P6-0', ), vector=(2.456, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P7']
a.Instance(name='P7-0', part=p, dependent=ON)
a.translate(instanceList=('P7-0', ), vector=(6.768000025087256, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P8']
a.Instance(name='P8-0', part=p, dependent=ON)
a.translate(instanceList=('P8-0', ), vector=(11.315958005881164, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P9']
a.Instance(name='P9-0', part=p, dependent=ON)
a.translate(instanceList=('P9-0', ), vector=(15.764804768921076, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P10']
a.Instance(name='P10-0', part=p, dependent=ON)
a.translate(instanceList=('P10-0', ), vector=(20.268862412528826, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P11']
a.Instance(name='P11-0', part=p, dependent=ON)
a.translate(instanceList=('P11-0', ), vector=(24.58086243237677, 0, 4.223143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P12']
a.Instance(name='P12-0', part=p, dependent=ON)
a.translate(instanceList=('P12-0', ), vector=(2.456, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P13']
a.Instance(name='P13-0', part=p, dependent=ON)
a.translate(instanceList=('P13-0', ), vector=(6.768000025087256, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P14']
a.Instance(name='P14-0', part=p, dependent=ON)
a.translate(instanceList=('P14-0', ), vector=(11.315958005881164, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P15']
a.Instance(name='P15-0', part=p, dependent=ON)
a.translate(instanceList=('P15-0', ), vector=(15.764804768921076, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P16']
a.Instance(name='P16-0', part=p, dependent=ON)
a.translate(instanceList=('P16-0', ), vector=(20.268862412528826, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P17']
a.Instance(name='P17-0', part=p, dependent=ON)
a.translate(instanceList=('P17-0', ), vector=(24.58086243237677, 0, 8.655415177501585))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P18']
a.Instance(name='P18-0', part=p, dependent=ON)
a.translate(instanceList=('P18-0', ), vector=(2.456, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P19']
a.Instance(name='P19-0', part=p, dependent=ON)
a.translate(instanceList=('P19-0', ), vector=(6.768000025087256, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P20']
a.Instance(name='P20-0', part=p, dependent=ON)
a.translate(instanceList=('P20-0', ), vector=(11.315958005881164, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P21']
a.Instance(name='P21-0', part=p, dependent=ON)
a.translate(instanceList=('P21-0', ), vector=(15.764804768921076, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P22']
a.Instance(name='P22-0', part=p, dependent=ON)
a.translate(instanceList=('P22-0', ), vector=(20.268862412528826, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P23']
a.Instance(name='P23-0', part=p, dependent=ON)
a.translate(instanceList=('P23-0', ), vector=(24.58086243237677, 0, 13.078703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P24']
a.Instance(name='P24-0', part=p, dependent=ON)
a.translate(instanceList=('P24-0', ), vector=(2.456, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P25']
a.Instance(name='P25-0', part=p, dependent=ON)
a.translate(instanceList=('P25-0', ), vector=(6.768000025087256, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P26']
a.Instance(name='P26-0', part=p, dependent=ON)
a.translate(instanceList=('P26-0', ), vector=(11.315958005881164, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P27']
a.Instance(name='P27-0', part=p, dependent=ON)
a.translate(instanceList=('P27-0', ), vector=(15.764804768921076, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P28']
a.Instance(name='P28-0', part=p, dependent=ON)
a.translate(instanceList=('P28-0', ), vector=(20.268862412528826, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P29']
a.Instance(name='P29-0', part=p, dependent=ON)
a.translate(instanceList=('P29-0', ), vector=(24.58086243237677, 0, 17.627007571214833))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P30']
a.Instance(name='P30-0', part=p, dependent=ON)
a.translate(instanceList=('P30-0', ), vector=(2.456, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P31']
a.Instance(name='P31-0', part=p, dependent=ON)
a.translate(instanceList=('P31-0', ), vector=(6.768000025087256, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P32']
a.Instance(name='P32-0', part=p, dependent=ON)
a.translate(instanceList=('P32-0', ), vector=(11.315958005881164, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P33']
a.Instance(name='P33-0', part=p, dependent=ON)
a.translate(instanceList=('P33-0', ), vector=(15.764804768921076, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P34']
a.Instance(name='P34-0', part=p, dependent=ON)
a.translate(instanceList=('P34-0', ), vector=(20.268862412528826, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P35']
a.Instance(name='P35-0', part=p, dependent=ON)
a.translate(instanceList=('P35-0', ), vector=(24.58086243237677, 0, 21.939007573658955))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P36']
a.Instance(name='P36-0', part=p, dependent=ON)
a.translate(instanceList=('P36-0', ), vector=(2.456, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P37']
a.Instance(name='P37-0', part=p, dependent=ON)
a.translate(instanceList=('P37-0', ), vector=(6.768000025087256, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P38']
a.Instance(name='P38-0', part=p, dependent=ON)
a.translate(instanceList=('P38-0', ), vector=(11.315958005881164, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P39']
a.Instance(name='P39-0', part=p, dependent=ON)
a.translate(instanceList=('P39-0', ), vector=(15.764804768921076, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P40']
a.Instance(name='P40-0', part=p, dependent=ON)
a.translate(instanceList=('P40-0', ), vector=(20.268862412528826, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P41']
a.Instance(name='P41-0', part=p, dependent=ON)
a.translate(instanceList=('P41-0', ), vector=(24.58086243237677, 0, 26.39824336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P42']
a.Instance(name='P42-0', part=p, dependent=ON)
a.translate(instanceList=('P42-0', ), vector=(2.456, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P43']
a.Instance(name='P43-0', part=p, dependent=ON)
a.translate(instanceList=('P43-0', ), vector=(6.768000025087256, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P44']
a.Instance(name='P44-0', part=p, dependent=ON)
a.translate(instanceList=('P44-0', ), vector=(11.315958005881164, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P45']
a.Instance(name='P45-0', part=p, dependent=ON)
a.translate(instanceList=('P45-0', ), vector=(15.764804768921076, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P46']
a.Instance(name='P46-0', part=p, dependent=ON)
a.translate(instanceList=('P46-0', ), vector=(20.268862412528826, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P47']
a.Instance(name='P47-0', part=p, dependent=ON)
a.translate(instanceList=('P47-0', ), vector=(24.58086243237677, 0, 30.79204832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P48']
a.Instance(name='P48-0', part=p, dependent=ON)
a.translate(instanceList=('P48-0', ), vector=(2.456, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P49']
a.Instance(name='P49-0', part=p, dependent=ON)
a.translate(instanceList=('P49-0', ), vector=(6.768000025087256, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P50']
a.Instance(name='P50-0', part=p, dependent=ON)
a.translate(instanceList=('P50-0', ), vector=(11.315958005881164, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P51']
a.Instance(name='P51-0', part=p, dependent=ON)
a.translate(instanceList=('P51-0', ), vector=(15.764804768921076, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P52']
a.Instance(name='P52-0', part=p, dependent=ON)
a.translate(instanceList=('P52-0', ), vector=(20.268862412528826, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P53']
a.Instance(name='P53-0', part=p, dependent=ON)
a.translate(instanceList=('P53-0', ), vector=(24.58086243237677, 0, 35.1089896459318))
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P54']
a.Instance(name='P54-0', part=p, dependent=ON)
a.translate(instanceList=('P54-0', ), vector=(1.248, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P54-0', ), axisPoint=(1.248, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P55']
a.Instance(name='P55-0', part=p, dependent=ON)
a.translate(instanceList=('P55-0', ), vector=(1.248, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P55-0', ), axisPoint=(1.248, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P56']
a.Instance(name='P56-0', part=p, dependent=ON)
a.translate(instanceList=('P56-0', ), vector=(1.248, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P56-0', ), axisPoint=(1.248, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P57']
a.Instance(name='P57-0', part=p, dependent=ON)
a.translate(instanceList=('P57-0', ), vector=(1.248, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P57-0', ), axisPoint=(1.248, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P58']
a.Instance(name='P58-0', part=p, dependent=ON)
a.translate(instanceList=('P58-0', ), vector=(1.248, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P58-0', ), axisPoint=(1.248, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P59']
a.Instance(name='P59-0', part=p, dependent=ON)
a.translate(instanceList=('P59-0', ), vector=(1.248, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P59-0', ), axisPoint=(1.248, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P60']
a.Instance(name='P60-0', part=p, dependent=ON)
a.translate(instanceList=('P60-0', ), vector=(1.248, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P60-0', ), axisPoint=(1.248, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P61']
a.Instance(name='P61-0', part=p, dependent=ON)
a.translate(instanceList=('P61-0', ), vector=(1.248, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P61-0', ), axisPoint=(1.248, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P62']
a.Instance(name='P62-0', part=p, dependent=ON)
a.translate(instanceList=('P62-0', ), vector=(5.560000025087255, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P62-0', ), axisPoint=(5.560000025087255, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P63']
a.Instance(name='P63-0', part=p, dependent=ON)
a.translate(instanceList=('P63-0', ), vector=(5.560000025087255, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P63-0', ), axisPoint=(5.560000025087255, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P64']
a.Instance(name='P64-0', part=p, dependent=ON)
a.translate(instanceList=('P64-0', ), vector=(5.560000025087255, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P64-0', ), axisPoint=(5.560000025087255, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P65']
a.Instance(name='P65-0', part=p, dependent=ON)
a.translate(instanceList=('P65-0', ), vector=(5.560000025087255, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P65-0', ), axisPoint=(5.560000025087255, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P66']
a.Instance(name='P66-0', part=p, dependent=ON)
a.translate(instanceList=('P66-0', ), vector=(5.560000025087255, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P66-0', ), axisPoint=(5.560000025087255, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P67']
a.Instance(name='P67-0', part=p, dependent=ON)
a.translate(instanceList=('P67-0', ), vector=(5.560000025087255, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P67-0', ), axisPoint=(5.560000025087255, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P68']
a.Instance(name='P68-0', part=p, dependent=ON)
a.translate(instanceList=('P68-0', ), vector=(5.560000025087255, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P68-0', ), axisPoint=(5.560000025087255, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P69']
a.Instance(name='P69-0', part=p, dependent=ON)
a.translate(instanceList=('P69-0', ), vector=(5.560000025087255, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P69-0', ), axisPoint=(5.560000025087255, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P70']
a.Instance(name='P70-0', part=p, dependent=ON)
a.translate(instanceList=('P70-0', ), vector=(10.107958005881162, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P70-0', ), axisPoint=(10.107958005881162, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P71']
a.Instance(name='P71-0', part=p, dependent=ON)
a.translate(instanceList=('P71-0', ), vector=(10.107958005881162, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P71-0', ), axisPoint=(10.107958005881162, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P72']
a.Instance(name='P72-0', part=p, dependent=ON)
a.translate(instanceList=('P72-0', ), vector=(10.107958005881162, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P72-0', ), axisPoint=(10.107958005881162, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P73']
a.Instance(name='P73-0', part=p, dependent=ON)
a.translate(instanceList=('P73-0', ), vector=(10.107958005881162, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P73-0', ), axisPoint=(10.107958005881162, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P74']
a.Instance(name='P74-0', part=p, dependent=ON)
a.translate(instanceList=('P74-0', ), vector=(10.107958005881162, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P74-0', ), axisPoint=(10.107958005881162, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P75']
a.Instance(name='P75-0', part=p, dependent=ON)
a.translate(instanceList=('P75-0', ), vector=(10.107958005881162, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P75-0', ), axisPoint=(10.107958005881162, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P76']
a.Instance(name='P76-0', part=p, dependent=ON)
a.translate(instanceList=('P76-0', ), vector=(10.107958005881162, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P76-0', ), axisPoint=(10.107958005881162, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P77']
a.Instance(name='P77-0', part=p, dependent=ON)
a.translate(instanceList=('P77-0', ), vector=(10.107958005881162, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P77-0', ), axisPoint=(10.107958005881162, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P78']
a.Instance(name='P78-0', part=p, dependent=ON)
a.translate(instanceList=('P78-0', ), vector=(14.556804768921076, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P78-0', ), axisPoint=(14.556804768921076, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P79']
a.Instance(name='P79-0', part=p, dependent=ON)
a.translate(instanceList=('P79-0', ), vector=(14.556804768921076, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P79-0', ), axisPoint=(14.556804768921076, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P80']
a.Instance(name='P80-0', part=p, dependent=ON)
a.translate(instanceList=('P80-0', ), vector=(14.556804768921076, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P80-0', ), axisPoint=(14.556804768921076, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P81']
a.Instance(name='P81-0', part=p, dependent=ON)
a.translate(instanceList=('P81-0', ), vector=(14.556804768921076, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P81-0', ), axisPoint=(14.556804768921076, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P82']
a.Instance(name='P82-0', part=p, dependent=ON)
a.translate(instanceList=('P82-0', ), vector=(14.556804768921076, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P82-0', ), axisPoint=(14.556804768921076, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P83']
a.Instance(name='P83-0', part=p, dependent=ON)
a.translate(instanceList=('P83-0', ), vector=(14.556804768921076, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P83-0', ), axisPoint=(14.556804768921076, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P84']
a.Instance(name='P84-0', part=p, dependent=ON)
a.translate(instanceList=('P84-0', ), vector=(14.556804768921076, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P84-0', ), axisPoint=(14.556804768921076, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P85']
a.Instance(name='P85-0', part=p, dependent=ON)
a.translate(instanceList=('P85-0', ), vector=(14.556804768921076, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P85-0', ), axisPoint=(14.556804768921076, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P86']
a.Instance(name='P86-0', part=p, dependent=ON)
a.translate(instanceList=('P86-0', ), vector=(19.060862412528827, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P86-0', ), axisPoint=(19.060862412528827, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P87']
a.Instance(name='P87-0', part=p, dependent=ON)
a.translate(instanceList=('P87-0', ), vector=(19.060862412528827, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P87-0', ), axisPoint=(19.060862412528827, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P88']
a.Instance(name='P88-0', part=p, dependent=ON)
a.translate(instanceList=('P88-0', ), vector=(19.060862412528827, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P88-0', ), axisPoint=(19.060862412528827, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P89']
a.Instance(name='P89-0', part=p, dependent=ON)
a.translate(instanceList=('P89-0', ), vector=(19.060862412528827, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P89-0', ), axisPoint=(19.060862412528827, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P90']
a.Instance(name='P90-0', part=p, dependent=ON)
a.translate(instanceList=('P90-0', ), vector=(19.060862412528827, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P90-0', ), axisPoint=(19.060862412528827, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P91']
a.Instance(name='P91-0', part=p, dependent=ON)
a.translate(instanceList=('P91-0', ), vector=(19.060862412528827, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P91-0', ), axisPoint=(19.060862412528827, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P92']
a.Instance(name='P92-0', part=p, dependent=ON)
a.translate(instanceList=('P92-0', ), vector=(19.060862412528827, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P92-0', ), axisPoint=(19.060862412528827, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P93']
a.Instance(name='P93-0', part=p, dependent=ON)
a.translate(instanceList=('P93-0', ), vector=(19.060862412528827, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P93-0', ), axisPoint=(19.060862412528827, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P94']
a.Instance(name='P94-0', part=p, dependent=ON)
a.translate(instanceList=('P94-0', ), vector=(23.37286243237677, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P94-0', ), axisPoint=(23.37286243237677, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P95']
a.Instance(name='P95-0', part=p, dependent=ON)
a.translate(instanceList=('P95-0', ), vector=(23.37286243237677, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P95-0', ), axisPoint=(23.37286243237677, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P96']
a.Instance(name='P96-0', part=p, dependent=ON)
a.translate(instanceList=('P96-0', ), vector=(23.37286243237677, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P96-0', ), axisPoint=(23.37286243237677, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P97']
a.Instance(name='P97-0', part=p, dependent=ON)
a.translate(instanceList=('P97-0', ), vector=(23.37286243237677, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P97-0', ), axisPoint=(23.37286243237677, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P98']
a.Instance(name='P98-0', part=p, dependent=ON)
a.translate(instanceList=('P98-0', ), vector=(23.37286243237677, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P98-0', ), axisPoint=(23.37286243237677, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P99']
a.Instance(name='P99-0', part=p, dependent=ON)
a.translate(instanceList=('P99-0', ), vector=(23.37286243237677, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P99-0', ), axisPoint=(23.37286243237677, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P100']
a.Instance(name='P100-0', part=p, dependent=ON)
a.translate(instanceList=('P100-0', ), vector=(23.37286243237677, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P100-0', ), axisPoint=(23.37286243237677, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P101']
a.Instance(name='P101-0', part=p, dependent=ON)
a.translate(instanceList=('P101-0', ), vector=(23.37286243237677, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P101-0', ), axisPoint=(23.37286243237677, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P102']
a.Instance(name='P102-0', part=p, dependent=ON)
a.translate(instanceList=('P102-0', ), vector=(27.855222856090023, 0, 1.1173))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P102-0', ), axisPoint=(27.855222856090023, 0, 2.456), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P103']
a.Instance(name='P103-0', part=p, dependent=ON)
a.translate(instanceList=('P103-0', ), vector=(27.855222856090023, 0, 5.527143525636163))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P103-0', ), axisPoint=(27.855222856090023, 0, 6.865843525636163), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P104']
a.Instance(name='P104-0', part=p, dependent=ON)
a.translate(instanceList=('P104-0', ), vector=(27.855222856090023, 0, 9.959415177501583))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P104-0', ), axisPoint=(27.855222856090023, 0, 11.298115177501582), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P105']
a.Instance(name='P105-0', part=p, dependent=ON)
a.translate(instanceList=('P105-0', ), vector=(27.855222856090023, 0, 14.382703289391582))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P105-0', ), axisPoint=(27.855222856090023, 0, 15.721403289391581), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P106']
a.Instance(name='P106-0', part=p, dependent=ON)
a.translate(instanceList=('P106-0', ), vector=(27.855222856090023, 0, 18.93100757121483))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P106-0', ), axisPoint=(27.855222856090023, 0, 20.26970757121483), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P107']
a.Instance(name='P107-0', part=p, dependent=ON)
a.translate(instanceList=('P107-0', ), vector=(27.855222856090023, 0, 23.243007573658957))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P107-0', ), axisPoint=(27.855222856090023, 0, 24.581707573658957), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P108']
a.Instance(name='P108-0', part=p, dependent=ON)
a.translate(instanceList=('P108-0', ), vector=(27.855222856090023, 0, 27.70224336852209))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P108-0', ), axisPoint=(27.855222856090023, 0, 29.04094336852209), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
p = mdb.models['Onerow_Stretch'].parts['P109']
a.Instance(name='P109-0', part=p, dependent=ON)
a.translate(instanceList=('P109-0', ), vector=(27.855222856090023, 0, 32.09604832900494))
a = mdb.models['Onerow_Stretch'].rootAssembly
a.rotate(instanceList=('P109-0', ), axisPoint=(27.855222856090023, 0, 33.43474832900494), axisDirection=(0.0, -1.0, 0.0), angle=90.0)
a = mdb.models['Onerow_Stretch'].rootAssembly
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_0_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-0'].edges.findAt (coordinates = ((2.456,0,1.1664441750401444),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_0_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P0-0'].edges.findAt (coordinates = ((2.456,0,1.1664441750401444), (2.456,0,1.1666441750401444),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_0_left_M'], name='Constraint-0_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_0_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_0_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-1'].edges.findAt (coordinates = ((4.256000025087256,0,1.1664441750401444),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_0_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P0-0'].edges.findAt (coordinates = ((4.256000025087256,0,1.1664441750401444), (4.256000025087256,0,1.1666441750401444,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_0_right_M'], name='Constraint-0_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_0_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_1_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-1'].edges.findAt (coordinates = ((6.768000025087256,0,1.16586105514488),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_1_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P1-0'].edges.findAt (coordinates = ((6.768000025087256,0,1.16586105514488), (6.768000025087256,0,1.16606105514488),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_1_left_M'], name='Constraint-1_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_1_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_1_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-2'].edges.findAt (coordinates = ((8.803958005881162,0,1.16586105514488),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_1_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P1-0'].edges.findAt (coordinates = ((8.803958005881162,0,1.16586105514488), (8.803958005881162,0,1.16606105514488,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_1_right_M'], name='Constraint-1_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_1_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_2_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-2'].edges.findAt (coordinates = ((11.315958005881164,0,1.1629455927022923),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_2_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P2-0'].edges.findAt (coordinates = ((11.315958005881164,0,1.1629455927022923), (11.315958005881164,0,1.1631455927022922),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_2_left_M'], name='Constraint-2_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_2_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_2_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-3'].edges.findAt (coordinates = ((13.252804768921077,0,1.1629455927022923),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_2_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P2-0'].edges.findAt (coordinates = ((13.252804768921077,0,1.1629455927022923), (13.252804768921077,0,1.1631455927022922,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_2_right_M'], name='Constraint-2_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_2_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_3_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-3'].edges.findAt (coordinates = ((15.764804768921076,0,1.1635585037328433),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_3_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P3-0'].edges.findAt (coordinates = ((15.764804768921076,0,1.1635585037328433), (15.764804768921076,0,1.1637585037328433),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_3_left_M'], name='Constraint-3_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_3_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_3_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-4'].edges.findAt (coordinates = ((17.756862412528825,0,1.1635585037328433),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_3_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P3-0'].edges.findAt (coordinates = ((17.756862412528825,0,1.1635585037328433), (17.756862412528825,0,1.1637585037328433,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_3_right_M'], name='Constraint-3_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_3_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_4_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-4'].edges.findAt (coordinates = ((20.268862412528826,0,1.1655822168487575),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_4_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P4-0'].edges.findAt (coordinates = ((20.268862412528826,0,1.1655822168487575), (20.268862412528826,0,1.1657822168487575),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_4_left_M'], name='Constraint-4_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_4_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_4_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-5'].edges.findAt (coordinates = ((22.06886243237677,0,1.1655822168487575),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_4_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P4-0'].edges.findAt (coordinates = ((22.06886243237677,0,1.1655822168487575), (22.06886243237677,0,1.1657822168487575,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_4_right_M'], name='Constraint-4_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_4_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_5_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-5'].edges.findAt (coordinates = ((24.58086243237677,0,1.1661629672485583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_5_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P5-0'].edges.findAt (coordinates = ((24.58086243237677,0,1.1661629672485583), (24.58086243237677,0,1.1663629672485583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_5_left_M'], name='Constraint-5_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_5_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_5_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-6'].edges.findAt (coordinates = ((26.55122285609002,0,1.1661629672485583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_5_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P5-0'].edges.findAt (coordinates = ((26.55122285609002,0,1.1661629672485583), (26.55122285609002,0,1.1663629672485583,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_5_right_M'], name='Constraint-5_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_5_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_6_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-7'].edges.findAt (coordinates = ((2.456,0,5.574896184200362),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_6_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P6-0'].edges.findAt (coordinates = ((2.456,0,5.574896184200362), (2.456,0,5.575096184200362),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_6_left_M'], name='Constraint-6_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_6_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_6_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-8'].edges.findAt (coordinates = ((4.256000025087256,0,5.574896184200362),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_6_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P6-0'].edges.findAt (coordinates = ((4.256000025087256,0,5.574896184200362), (4.256000025087256,0,5.575096184200362,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_6_right_M'], name='Constraint-6_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_6_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_7_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-8'].edges.findAt (coordinates = ((6.768000025087256,0,5.5722709160782635),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_7_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P7-0'].edges.findAt (coordinates = ((6.768000025087256,0,5.5722709160782635), (6.768000025087256,0,5.572470916078263),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_7_left_M'], name='Constraint-7_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_7_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_7_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-9'].edges.findAt (coordinates = ((8.803958005881162,0,5.5722709160782635),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_7_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P7-0'].edges.findAt (coordinates = ((8.803958005881162,0,5.5722709160782635), (8.803958005881162,0,5.572470916078263,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_7_right_M'], name='Constraint-7_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_7_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_8_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-9'].edges.findAt (coordinates = ((11.315958005881164,0,5.566743525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_8_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P8-0'].edges.findAt (coordinates = ((11.315958005881164,0,5.566743525636163), (11.315958005881164,0,5.566943525636162),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_8_left_M'], name='Constraint-8_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_8_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_8_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-10'].edges.findAt (coordinates = ((13.252804768921077,0,5.566743525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_8_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P8-0'].edges.findAt (coordinates = ((13.252804768921077,0,5.566743525636163), (13.252804768921077,0,5.566943525636162,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_8_right_M'], name='Constraint-8_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_8_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_9_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-10'].edges.findAt (coordinates = ((15.764804768921076,0,5.573115742615015),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_9_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P9-0'].edges.findAt (coordinates = ((15.764804768921076,0,5.573115742615015), (15.764804768921076,0,5.573315742615015),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_9_left_M'], name='Constraint-9_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_9_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_9_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-11'].edges.findAt (coordinates = ((17.756862412528825,0,5.573115742615015),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_9_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P9-0'].edges.findAt (coordinates = ((17.756862412528825,0,5.573115742615015), (17.756862412528825,0,5.573315742615015,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_9_right_M'], name='Constraint-9_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_9_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_10_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-11'].edges.findAt (coordinates = ((20.268862412528826,0,5.569603225043477),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_10_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P10-0'].edges.findAt (coordinates = ((20.268862412528826,0,5.569603225043477), (20.268862412528826,0,5.569803225043477),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_10_left_M'], name='Constraint-10_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_10_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_10_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-12'].edges.findAt (coordinates = ((22.06886243237677,0,5.569603225043477),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_10_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P10-0'].edges.findAt (coordinates = ((22.06886243237677,0,5.569603225043477), (22.06886243237677,0,5.569803225043477,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_10_right_M'], name='Constraint-10_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_10_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_11_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-12'].edges.findAt (coordinates = ((24.58086243237677,0,5.569331391962375),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_11_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P11-0'].edges.findAt (coordinates = ((24.58086243237677,0,5.569331391962375), (24.58086243237677,0,5.569531391962374),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_11_left_M'], name='Constraint-11_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_11_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_11_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-13'].edges.findAt (coordinates = ((26.55122285609002,0,5.569331391962375),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_11_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P11-0'].edges.findAt (coordinates = ((26.55122285609002,0,5.569331391962375), (26.55122285609002,0,5.569531391962374,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_11_right_M'], name='Constraint-11_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_11_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_12_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-14'].edges.findAt (coordinates = ((2.456,0,10.00168391852788),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_12_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P12-0'].edges.findAt (coordinates = ((2.456,0,10.00168391852788), (2.456,0,10.001883918527879),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_12_left_M'], name='Constraint-12_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_12_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_12_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-15'].edges.findAt (coordinates = ((4.256000025087256,0,10.00168391852788),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_12_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P12-0'].edges.findAt (coordinates = ((4.256000025087256,0,10.00168391852788), (4.256000025087256,0,10.001883918527879,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_12_right_M'], name='Constraint-12_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_12_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_13_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-15'].edges.findAt (coordinates = ((6.768000025087256,0,10.00416260145855),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_13_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P13-0'].edges.findAt (coordinates = ((6.768000025087256,0,10.00416260145855), (6.768000025087256,0,10.00436260145855),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_13_left_M'], name='Constraint-13_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_13_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_13_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-16'].edges.findAt (coordinates = ((8.803958005881162,0,10.00416260145855),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_13_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P13-0'].edges.findAt (coordinates = ((8.803958005881162,0,10.00416260145855), (8.803958005881162,0,10.00436260145855,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_13_right_M'], name='Constraint-13_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_13_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_14_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-16'].edges.findAt (coordinates = ((11.315958005881164,0,10.004062248724669),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_14_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P14-0'].edges.findAt (coordinates = ((11.315958005881164,0,10.004062248724669), (11.315958005881164,0,10.004262248724668),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_14_left_M'], name='Constraint-14_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_14_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_14_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-17'].edges.findAt (coordinates = ((13.252804768921077,0,10.004062248724669),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_14_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P14-0'].edges.findAt (coordinates = ((13.252804768921077,0,10.004062248724669), (13.252804768921077,0,10.004262248724668,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_14_right_M'], name='Constraint-14_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_14_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_15_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-17'].edges.findAt (coordinates = ((15.764804768921076,0,10.009015177501585),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_15_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P15-0'].edges.findAt (coordinates = ((15.764804768921076,0,10.009015177501585), (15.764804768921076,0,10.009215177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_15_left_M'], name='Constraint-15_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_15_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_15_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-18'].edges.findAt (coordinates = ((17.756862412528825,0,10.009015177501585),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_15_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P15-0'].edges.findAt (coordinates = ((17.756862412528825,0,10.009015177501585), (17.756862412528825,0,10.009215177501584,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_15_right_M'], name='Constraint-15_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_15_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_16_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-18'].edges.findAt (coordinates = ((20.268862412528826,0,10.009015177501585),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_16_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P16-0'].edges.findAt (coordinates = ((20.268862412528826,0,10.009015177501585), (20.268862412528826,0,10.009215177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_16_left_M'], name='Constraint-16_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_16_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_16_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-19'].edges.findAt (coordinates = ((22.06886243237677,0,10.009015177501585),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_16_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P16-0'].edges.findAt (coordinates = ((22.06886243237677,0,10.009015177501585), (22.06886243237677,0,10.009215177501584,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_16_right_M'], name='Constraint-16_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_16_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_17_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-19'].edges.findAt (coordinates = ((24.58086243237677,0,10.008872441758951),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_17_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P17-0'].edges.findAt (coordinates = ((24.58086243237677,0,10.008872441758951), (24.58086243237677,0,10.009072441758951),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_17_left_M'], name='Constraint-17_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_17_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_17_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-20'].edges.findAt (coordinates = ((26.55122285609002,0,10.008872441758951),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_17_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P17-0'].edges.findAt (coordinates = ((26.55122285609002,0,10.008872441758951), (26.55122285609002,0,10.009072441758951,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_17_right_M'], name='Constraint-17_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_17_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_18_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-21'].edges.findAt (coordinates = ((2.456,0,14.427956525829323),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_18_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P18-0'].edges.findAt (coordinates = ((2.456,0,14.427956525829323), (2.456,0,14.428156525829323),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_18_left_M'], name='Constraint-18_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_18_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_18_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-22'].edges.findAt (coordinates = ((4.256000025087256,0,14.427956525829323),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_18_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P18-0'].edges.findAt (coordinates = ((4.256000025087256,0,14.427956525829323), (4.256000025087256,0,14.428156525829323,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_18_right_M'], name='Constraint-18_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_18_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_19_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-22'].edges.findAt (coordinates = ((6.768000025087256,0,14.422303289391582),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_19_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P19-0'].edges.findAt (coordinates = ((6.768000025087256,0,14.422303289391582), (6.768000025087256,0,14.422503289391582),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_19_left_M'], name='Constraint-19_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_19_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_19_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-23'].edges.findAt (coordinates = ((8.803958005881162,0,14.422303289391582),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_19_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P19-0'].edges.findAt (coordinates = ((8.803958005881162,0,14.422303289391582), (8.803958005881162,0,14.422503289391582,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_19_right_M'], name='Constraint-19_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_19_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_20_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-23'].edges.findAt (coordinates = ((11.315958005881164,0,14.424447702697933),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_20_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P20-0'].edges.findAt (coordinates = ((11.315958005881164,0,14.424447702697933), (11.315958005881164,0,14.424647702697932),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_20_left_M'], name='Constraint-20_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_20_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_20_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-24'].edges.findAt (coordinates = ((13.252804768921077,0,14.424447702697933),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_20_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P20-0'].edges.findAt (coordinates = ((13.252804768921077,0,14.424447702697933), (13.252804768921077,0,14.424647702697932,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_20_right_M'], name='Constraint-20_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_20_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_21_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-24'].edges.findAt (coordinates = ((15.764804768921076,0,14.430010941915993),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_21_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P21-0'].edges.findAt (coordinates = ((15.764804768921076,0,14.430010941915993), (15.764804768921076,0,14.430210941915993),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_21_left_M'], name='Constraint-21_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_21_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_21_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-25'].edges.findAt (coordinates = ((17.756862412528825,0,14.430010941915993),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_21_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P21-0'].edges.findAt (coordinates = ((17.756862412528825,0,14.430010941915993), (17.756862412528825,0,14.430210941915993,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_21_right_M'], name='Constraint-21_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_21_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_22_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-25'].edges.findAt (coordinates = ((20.268862412528826,0,14.4299483192393),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_22_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P22-0'].edges.findAt (coordinates = ((20.268862412528826,0,14.4299483192393), (20.268862412528826,0,14.430148319239299),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_22_left_M'], name='Constraint-22_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_22_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_22_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-26'].edges.findAt (coordinates = ((22.06886243237677,0,14.4299483192393),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_22_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P22-0'].edges.findAt (coordinates = ((22.06886243237677,0,14.4299483192393), (22.06886243237677,0,14.430148319239299,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_22_right_M'], name='Constraint-22_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_22_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_23_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-26'].edges.findAt (coordinates = ((24.58086243237677,0,14.43187024719231),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_23_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P23-0'].edges.findAt (coordinates = ((24.58086243237677,0,14.43187024719231), (24.58086243237677,0,14.432070247192309),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_23_left_M'], name='Constraint-23_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_23_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_23_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-27'].edges.findAt (coordinates = ((26.55122285609002,0,14.43187024719231),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_23_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P23-0'].edges.findAt (coordinates = ((26.55122285609002,0,14.43187024719231), (26.55122285609002,0,14.432070247192309,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_23_right_M'], name='Constraint-23_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_23_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_24_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-28'].edges.findAt (coordinates = ((2.456,0,18.98060757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_24_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P24-0'].edges.findAt (coordinates = ((2.456,0,18.98060757121483), (2.456,0,18.98080757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_24_left_M'], name='Constraint-24_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_24_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_24_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-29'].edges.findAt (coordinates = ((4.256000025087256,0,18.98060757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_24_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P24-0'].edges.findAt (coordinates = ((4.256000025087256,0,18.98060757121483), (4.256000025087256,0,18.98080757121483,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_24_right_M'], name='Constraint-24_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_24_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_25_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-29'].edges.findAt (coordinates = ((6.768000025087256,0,18.977130176476965),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_25_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P25-0'].edges.findAt (coordinates = ((6.768000025087256,0,18.977130176476965), (6.768000025087256,0,18.977330176476965),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_25_left_M'], name='Constraint-25_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_25_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_25_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-30'].edges.findAt (coordinates = ((8.803958005881162,0,18.977130176476965),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_25_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P25-0'].edges.findAt (coordinates = ((8.803958005881162,0,18.977130176476965), (8.803958005881162,0,18.977330176476965,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_25_right_M'], name='Constraint-25_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_25_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_26_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-30'].edges.findAt (coordinates = ((11.315958005881164,0,18.980189080711288),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_26_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P26-0'].edges.findAt (coordinates = ((11.315958005881164,0,18.980189080711288), (11.315958005881164,0,18.980389080711287),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_26_left_M'], name='Constraint-26_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_26_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_26_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-31'].edges.findAt (coordinates = ((13.252804768921077,0,18.980189080711288),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_26_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P26-0'].edges.findAt (coordinates = ((13.252804768921077,0,18.980189080711288), (13.252804768921077,0,18.980389080711287,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_26_right_M'], name='Constraint-26_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_26_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_27_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-31'].edges.findAt (coordinates = ((15.764804768921076,0,18.980086340502982),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_27_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P27-0'].edges.findAt (coordinates = ((15.764804768921076,0,18.980086340502982), (15.764804768921076,0,18.980286340502982),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_27_left_M'], name='Constraint-27_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_27_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_27_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-32'].edges.findAt (coordinates = ((17.756862412528825,0,18.980086340502982),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_27_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P27-0'].edges.findAt (coordinates = ((17.756862412528825,0,18.980086340502982), (17.756862412528825,0,18.980286340502982,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_27_right_M'], name='Constraint-27_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_27_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_28_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-32'].edges.findAt (coordinates = ((20.268862412528826,0,18.978402081131016),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_28_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P28-0'].edges.findAt (coordinates = ((20.268862412528826,0,18.978402081131016), (20.268862412528826,0,18.978602081131015),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_28_left_M'], name='Constraint-28_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_28_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_28_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-33'].edges.findAt (coordinates = ((22.06886243237677,0,18.978402081131016),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_28_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P28-0'].edges.findAt (coordinates = ((22.06886243237677,0,18.978402081131016), (22.06886243237677,0,18.978602081131015,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_28_right_M'], name='Constraint-28_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_28_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_29_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-33'].edges.findAt (coordinates = ((24.58086243237677,0,18.98060757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_29_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P29-0'].edges.findAt (coordinates = ((24.58086243237677,0,18.98060757121483), (24.58086243237677,0,18.98080757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_29_left_M'], name='Constraint-29_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_29_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_29_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-34'].edges.findAt (coordinates = ((26.55122285609002,0,18.98060757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_29_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P29-0'].edges.findAt (coordinates = ((26.55122285609002,0,18.98060757121483), (26.55122285609002,0,18.98080757121483,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_29_right_M'], name='Constraint-29_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_29_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_30_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-35'].edges.findAt (coordinates = ((2.456,0,23.292607573658955),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_30_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P30-0'].edges.findAt (coordinates = ((2.456,0,23.292607573658955), (2.456,0,23.292807573658955),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_30_left_M'], name='Constraint-30_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_30_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_30_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-36'].edges.findAt (coordinates = ((4.256000025087256,0,23.292607573658955),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_30_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P30-0'].edges.findAt (coordinates = ((4.256000025087256,0,23.292607573658955), (4.256000025087256,0,23.292807573658955,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_30_right_M'], name='Constraint-30_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_30_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_31_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-36'].edges.findAt (coordinates = ((6.768000025087256,0,23.290303967192923),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_31_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P31-0'].edges.findAt (coordinates = ((6.768000025087256,0,23.290303967192923), (6.768000025087256,0,23.290503967192922),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_31_left_M'], name='Constraint-31_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_31_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_31_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-37'].edges.findAt (coordinates = ((8.803958005881162,0,23.290303967192923),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_31_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P31-0'].edges.findAt (coordinates = ((8.803958005881162,0,23.290303967192923), (8.803958005881162,0,23.290503967192922,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_31_right_M'], name='Constraint-31_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_31_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_32_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-37'].edges.findAt (coordinates = ((11.315958005881164,0,23.289033557655895),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_32_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P32-0'].edges.findAt (coordinates = ((11.315958005881164,0,23.289033557655895), (11.315958005881164,0,23.289233557655894),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_32_left_M'], name='Constraint-32_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_32_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_32_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-38'].edges.findAt (coordinates = ((13.252804768921077,0,23.289033557655895),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_32_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P32-0'].edges.findAt (coordinates = ((13.252804768921077,0,23.289033557655895), (13.252804768921077,0,23.289233557655894,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_32_right_M'], name='Constraint-32_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_32_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_33_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-38'].edges.findAt (coordinates = ((15.764804768921076,0,23.284126081816094),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_33_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P33-0'].edges.findAt (coordinates = ((15.764804768921076,0,23.284126081816094), (15.764804768921076,0,23.284326081816094),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_33_left_M'], name='Constraint-33_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_33_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_33_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-39'].edges.findAt (coordinates = ((17.756862412528825,0,23.284126081816094),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_33_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P33-0'].edges.findAt (coordinates = ((17.756862412528825,0,23.284126081816094), (17.756862412528825,0,23.284326081816094,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_33_right_M'], name='Constraint-33_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_33_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_34_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-39'].edges.findAt (coordinates = ((20.268862412528826,0,23.282607573658954),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_34_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P34-0'].edges.findAt (coordinates = ((20.268862412528826,0,23.282607573658954), (20.268862412528826,0,23.282807573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_34_left_M'], name='Constraint-34_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_34_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_34_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-40'].edges.findAt (coordinates = ((22.06886243237677,0,23.282607573658954),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_34_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P34-0'].edges.findAt (coordinates = ((22.06886243237677,0,23.282607573658954), (22.06886243237677,0,23.282807573658953,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_34_right_M'], name='Constraint-34_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_34_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_35_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-40'].edges.findAt (coordinates = ((24.58086243237677,0,23.286298305017706),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_35_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P35-0'].edges.findAt (coordinates = ((24.58086243237677,0,23.286298305017706), (24.58086243237677,0,23.286498305017705),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_35_left_M'], name='Constraint-35_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_35_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_35_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-41'].edges.findAt (coordinates = ((26.55122285609002,0,23.286298305017706),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_35_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P35-0'].edges.findAt (coordinates = ((26.55122285609002,0,23.286298305017706), (26.55122285609002,0,23.286498305017705,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_35_right_M'], name='Constraint-35_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_35_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_36_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-42'].edges.findAt (coordinates = ((2.456,0,27.75172660079284),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_36_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P36-0'].edges.findAt (coordinates = ((2.456,0,27.75172660079284), (2.456,0,27.75192660079284),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_36_left_M'], name='Constraint-36_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_36_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_36_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-43'].edges.findAt (coordinates = ((4.256000025087256,0,27.75172660079284),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_36_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P36-0'].edges.findAt (coordinates = ((4.256000025087256,0,27.75172660079284), (4.256000025087256,0,27.75192660079284,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_36_right_M'], name='Constraint-36_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_36_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_37_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-43'].edges.findAt (coordinates = ((6.768000025087256,0,27.751843368522092),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_37_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P37-0'].edges.findAt (coordinates = ((6.768000025087256,0,27.751843368522092), (6.768000025087256,0,27.75204336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_37_left_M'], name='Constraint-37_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_37_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_37_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-44'].edges.findAt (coordinates = ((8.803958005881162,0,27.751843368522092),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_37_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P37-0'].edges.findAt (coordinates = ((8.803958005881162,0,27.751843368522092), (8.803958005881162,0,27.75204336852209,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_37_right_M'], name='Constraint-37_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_37_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_38_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-44'].edges.findAt (coordinates = ((11.315958005881164,0,27.751843368522092),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_38_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P38-0'].edges.findAt (coordinates = ((11.315958005881164,0,27.751843368522092), (11.315958005881164,0,27.75204336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_38_left_M'], name='Constraint-38_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_38_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_38_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-45'].edges.findAt (coordinates = ((13.252804768921077,0,27.751843368522092),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_38_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P38-0'].edges.findAt (coordinates = ((13.252804768921077,0,27.751843368522092), (13.252804768921077,0,27.75204336852209,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_38_right_M'], name='Constraint-38_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_38_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_39_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-45'].edges.findAt (coordinates = ((15.764804768921076,0,27.74675135779942),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_39_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P39-0'].edges.findAt (coordinates = ((15.764804768921076,0,27.74675135779942), (15.764804768921076,0,27.746951357799418),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_39_left_M'], name='Constraint-39_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_39_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_39_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-46'].edges.findAt (coordinates = ((17.756862412528825,0,27.74675135779942),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_39_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P39-0'].edges.findAt (coordinates = ((17.756862412528825,0,27.74675135779942), (17.756862412528825,0,27.746951357799418,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_39_right_M'], name='Constraint-39_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_39_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_40_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-46'].edges.findAt (coordinates = ((20.268862412528826,0,27.745652658363696),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_40_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P40-0'].edges.findAt (coordinates = ((20.268862412528826,0,27.745652658363696), (20.268862412528826,0,27.745852658363695),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_40_left_M'], name='Constraint-40_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_40_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_40_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-47'].edges.findAt (coordinates = ((22.06886243237677,0,27.745652658363696),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_40_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P40-0'].edges.findAt (coordinates = ((22.06886243237677,0,27.745652658363696), (22.06886243237677,0,27.745852658363695,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_40_right_M'], name='Constraint-40_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_40_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_41_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-47'].edges.findAt (coordinates = ((24.58086243237677,0,27.74674536557364),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_41_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P41-0'].edges.findAt (coordinates = ((24.58086243237677,0,27.74674536557364), (24.58086243237677,0,27.74694536557364),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_41_left_M'], name='Constraint-41_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_41_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_41_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-48'].edges.findAt (coordinates = ((26.55122285609002,0,27.74674536557364),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_41_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P41-0'].edges.findAt (coordinates = ((26.55122285609002,0,27.74674536557364), (26.55122285609002,0,27.74694536557364,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_41_right_M'], name='Constraint-41_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_41_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_42_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-49'].edges.findAt (coordinates = ((2.456,0,32.14206077301162),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_42_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P42-0'].edges.findAt (coordinates = ((2.456,0,32.14206077301162), (2.456,0,32.14226077301163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_42_left_M'], name='Constraint-42_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_42_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_42_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-50'].edges.findAt (coordinates = ((4.256000025087256,0,32.14206077301162),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_42_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P42-0'].edges.findAt (coordinates = ((4.256000025087256,0,32.14206077301162), (4.256000025087256,0,32.14226077301163,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_42_right_M'], name='Constraint-42_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_42_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_43_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-50'].edges.findAt (coordinates = ((6.768000025087256,0,32.14125137555127),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_43_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P43-0'].edges.findAt (coordinates = ((6.768000025087256,0,32.14125137555127), (6.768000025087256,0,32.14145137555128),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_43_left_M'], name='Constraint-43_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_43_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_43_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-51'].edges.findAt (coordinates = ((8.803958005881162,0,32.14125137555127),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_43_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P43-0'].edges.findAt (coordinates = ((8.803958005881162,0,32.14125137555127), (8.803958005881162,0,32.14145137555128,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_43_right_M'], name='Constraint-43_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_43_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_44_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-51'].edges.findAt (coordinates = ((11.315958005881164,0,32.14182438394776),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_44_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P44-0'].edges.findAt (coordinates = ((11.315958005881164,0,32.14182438394776), (11.315958005881164,0,32.14202438394776),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_44_left_M'], name='Constraint-44_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_44_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_44_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-52'].edges.findAt (coordinates = ((13.252804768921077,0,32.14182438394776),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_44_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P44-0'].edges.findAt (coordinates = ((13.252804768921077,0,32.14182438394776), (13.252804768921077,0,32.14202438394776,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_44_right_M'], name='Constraint-44_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_44_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_45_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-52'].edges.findAt (coordinates = ((15.764804768921076,0,32.13564832900494),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_45_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P45-0'].edges.findAt (coordinates = ((15.764804768921076,0,32.13564832900494), (15.764804768921076,0,32.13584832900494),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_45_left_M'], name='Constraint-45_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_45_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_45_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-53'].edges.findAt (coordinates = ((17.756862412528825,0,32.13564832900494),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_45_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P45-0'].edges.findAt (coordinates = ((17.756862412528825,0,32.13564832900494), (17.756862412528825,0,32.13584832900494,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_45_right_M'], name='Constraint-45_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_45_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_46_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-53'].edges.findAt (coordinates = ((20.268862412528826,0,32.14032018072843),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_46_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P46-0'].edges.findAt (coordinates = ((20.268862412528826,0,32.14032018072843), (20.268862412528826,0,32.14052018072844),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_46_left_M'], name='Constraint-46_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_46_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_46_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-54'].edges.findAt (coordinates = ((22.06886243237677,0,32.14032018072843),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_46_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P46-0'].edges.findAt (coordinates = ((22.06886243237677,0,32.14032018072843), (22.06886243237677,0,32.14052018072844,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_46_right_M'], name='Constraint-46_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_46_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_47_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-54'].edges.findAt (coordinates = ((24.58086243237677,0,32.14329464510447),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_47_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P47-0'].edges.findAt (coordinates = ((24.58086243237677,0,32.14329464510447), (24.58086243237677,0,32.143494645104475),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_47_left_M'], name='Constraint-47_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_47_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_47_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-55'].edges.findAt (coordinates = ((26.55122285609002,0,32.14329464510447),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_47_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P47-0'].edges.findAt (coordinates = ((26.55122285609002,0,32.14329464510447), (26.55122285609002,0,32.143494645104475,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_47_right_M'], name='Constraint-47_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_47_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_48_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-56'].edges.findAt (coordinates = ((2.456,0,36.46148667794541),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_48_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P48-0'].edges.findAt (coordinates = ((2.456,0,36.46148667794541), (2.456,0,36.461686677945416),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_48_left_M'], name='Constraint-48_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_48_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_48_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-57'].edges.findAt (coordinates = ((4.256000025087256,0,36.46148667794541),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_48_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P48-0'].edges.findAt (coordinates = ((4.256000025087256,0,36.46148667794541), (4.256000025087256,0,36.461686677945416,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_48_right_M'], name='Constraint-48_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_48_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_49_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-57'].edges.findAt (coordinates = ((6.768000025087256,0,36.46193028419769),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_49_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P49-0'].edges.findAt (coordinates = ((6.768000025087256,0,36.46193028419769), (6.768000025087256,0,36.4621302841977),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_49_left_M'], name='Constraint-49_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_49_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_49_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-58'].edges.findAt (coordinates = ((8.803958005881162,0,36.46193028419769),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_49_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P49-0'].edges.findAt (coordinates = ((8.803958005881162,0,36.46193028419769), (8.803958005881162,0,36.4621302841977,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_49_right_M'], name='Constraint-49_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_49_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_50_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-58'].edges.findAt (coordinates = ((11.315958005881164,0,36.45706641022626),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_50_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P50-0'].edges.findAt (coordinates = ((11.315958005881164,0,36.45706641022626), (11.315958005881164,0,36.45726641022627),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_50_left_M'], name='Constraint-50_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_50_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_50_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-59'].edges.findAt (coordinates = ((13.252804768921077,0,36.45706641022626),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_50_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P50-0'].edges.findAt (coordinates = ((13.252804768921077,0,36.45706641022626), (13.252804768921077,0,36.45726641022627,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_50_right_M'], name='Constraint-50_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_50_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_51_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-59'].edges.findAt (coordinates = ((15.764804768921076,0,36.45732171865718),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_51_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P51-0'].edges.findAt (coordinates = ((15.764804768921076,0,36.45732171865718), (15.764804768921076,0,36.45752171865718),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_51_left_M'], name='Constraint-51_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_51_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_51_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-60'].edges.findAt (coordinates = ((17.756862412528825,0,36.45732171865718),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_51_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P51-0'].edges.findAt (coordinates = ((17.756862412528825,0,36.45732171865718), (17.756862412528825,0,36.45752171865718,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_51_right_M'], name='Constraint-51_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_51_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_52_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-60'].edges.findAt (coordinates = ((20.268862412528826,0,36.462485786771296),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_52_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P52-0'].edges.findAt (coordinates = ((20.268862412528826,0,36.462485786771296), (20.268862412528826,0,36.4626857867713),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_52_left_M'], name='Constraint-52_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_52_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_52_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-61'].edges.findAt (coordinates = ((22.06886243237677,0,36.462485786771296),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_52_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P52-0'].edges.findAt (coordinates = ((22.06886243237677,0,36.462485786771296), (22.06886243237677,0,36.4626857867713,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_52_right_M'], name='Constraint-52_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_52_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_53_left_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-61'].edges.findAt (coordinates = ((24.58086243237677,0,36.46258964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_53_left_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P53-0'].edges.findAt (coordinates = ((24.58086243237677,0,36.46258964593179), (24.58086243237677,0,36.4627896459318),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_53_left_M'], name='Constraint-53_left', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_53_left_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_53_right_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-62'].edges.findAt (coordinates = ((26.55122285609002,0,36.46258964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_53_right_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P53-0'].edges.findAt (coordinates = ((26.55122285609002,0,36.46258964593179), (26.55122285609002,0,36.4627896459318,))))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_53_right_M'], name='Constraint-53_right', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_53_right_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_54_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-0'].edges.findAt (coordinates = ((1.2396828820368533,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_54_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P54-0'].edges.findAt (coordinates = ((1.2396828820368533,0,2.456), (1.2398828820368533,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_54_up_M'], name='Constraint-54_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_54_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_54_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-7'].edges.findAt (coordinates = ((1.2396828820368533,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_54_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P54-0'].edges.findAt (coordinates = ((1.2396828820368533,0,4.353843525636163), (1.2398828820368533,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_54_low_M'], name='Constraint-54_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_54_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_55_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-7'].edges.findAt (coordinates = ((1.2386671131932743,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_55_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P55-0'].edges.findAt (coordinates = ((1.2386671131932743,0,6.865843525636163), (1.2388671131932742,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_55_up_M'], name='Constraint-55_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_55_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_55_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-14'].edges.findAt (coordinates = ((1.2386671131932743,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_55_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P55-0'].edges.findAt (coordinates = ((1.2386671131932743,0,8.786115177501584), (1.2388671131932742,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_55_low_M'], name='Constraint-55_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_55_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_56_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-14'].edges.findAt (coordinates = ((1.2369911784656542,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_56_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P56-0'].edges.findAt (coordinates = ((1.2369911784656542,0,11.298115177501584), (1.2371911784656542,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_56_up_M'], name='Constraint-56_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_56_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_56_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-21'].edges.findAt (coordinates = ((1.2369911784656542,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_56_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P56-0'].edges.findAt (coordinates = ((1.2369911784656542,0,13.209403289391583), (1.2371911784656542,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_56_low_M'], name='Constraint-56_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_56_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_57_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-21'].edges.findAt (coordinates = ((1.2371428835797773,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_57_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P57-0'].edges.findAt (coordinates = ((1.2371428835797773,0,15.721403289391581), (1.2373428835797773,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_57_up_M'], name='Constraint-57_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_57_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_57_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-28'].edges.findAt (coordinates = ((1.2371428835797773,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_57_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P57-0'].edges.findAt (coordinates = ((1.2371428835797773,0,17.75770757121483), (1.2373428835797773,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_57_low_M'], name='Constraint-57_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_57_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_58_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-28'].edges.findAt (coordinates = ((1.2365353313668341,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_58_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P58-0'].edges.findAt (coordinates = ((1.2365353313668341,0,20.26970757121483), (1.2367353313668341,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_58_up_M'], name='Constraint-58_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_58_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_58_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-35'].edges.findAt (coordinates = ((1.2365353313668341,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_58_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P58-0'].edges.findAt (coordinates = ((1.2365353313668341,0,22.069707573658953), (1.2367353313668341,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_58_low_M'], name='Constraint-58_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_58_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_59_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-35'].edges.findAt (coordinates = ((1.2329,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_59_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P59-0'].edges.findAt (coordinates = ((1.2329,0,24.581707573658953), (1.2331,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_59_up_M'], name='Constraint-59_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_59_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_59_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-42'].edges.findAt (coordinates = ((1.2329,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_59_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P59-0'].edges.findAt (coordinates = ((1.2329,0,26.52894336852209), (1.2331,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_59_low_M'], name='Constraint-59_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_59_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_60_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-42'].edges.findAt (coordinates = ((1.2329,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_60_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P60-0'].edges.findAt (coordinates = ((1.2329,0,29.04094336852209), (1.2331,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_60_up_M'], name='Constraint-60_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_60_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_60_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-49'].edges.findAt (coordinates = ((1.2329,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_60_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P60-0'].edges.findAt (coordinates = ((1.2329,0,30.922748329004936), (1.2331,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_60_low_M'], name='Constraint-60_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_60_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_61_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-49'].edges.findAt (coordinates = ((1.235794262267708,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_61_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P61-0'].edges.findAt (coordinates = ((1.235794262267708,0,33.43474832900493), (1.235994262267708,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_61_up_M'], name='Constraint-61_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_61_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_61_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-56'].edges.findAt (coordinates = ((1.235794262267708,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_61_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P61-0'].edges.findAt (coordinates = ((1.235794262267708,0,35.23968964593179), (1.235994262267708,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_61_low_M'], name='Constraint-61_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_61_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_62_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-1'].edges.findAt (coordinates = ((5.553731020691751,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_62_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P62-0'].edges.findAt (coordinates = ((5.553731020691751,0,2.456), (5.553931020691751,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_62_up_M'], name='Constraint-62_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_62_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_62_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-8'].edges.findAt (coordinates = ((5.553731020691751,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_62_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P62-0'].edges.findAt (coordinates = ((5.553731020691751,0,4.353843525636163), (5.553931020691751,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_62_low_M'], name='Constraint-62_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_62_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_63_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-8'].edges.findAt (coordinates = ((5.544900025087256,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_63_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P63-0'].edges.findAt (coordinates = ((5.544900025087256,0,6.865843525636163), (5.5451000250872555,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_63_up_M'], name='Constraint-63_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_63_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_63_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-15'].edges.findAt (coordinates = ((5.544900025087256,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_63_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P63-0'].edges.findAt (coordinates = ((5.544900025087256,0,8.786115177501584), (5.5451000250872555,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_63_low_M'], name='Constraint-63_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_63_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_64_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-15'].edges.findAt (coordinates = ((5.546054295389551,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_64_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P64-0'].edges.findAt (coordinates = ((5.546054295389551,0,11.298115177501584), (5.54625429538955,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_64_up_M'], name='Constraint-64_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_64_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_64_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-22'].edges.findAt (coordinates = ((5.546054295389551,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_64_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P64-0'].edges.findAt (coordinates = ((5.546054295389551,0,13.209403289391583), (5.54625429538955,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_64_low_M'], name='Constraint-64_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_64_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_65_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-22'].edges.findAt (coordinates = ((5.545918928706041,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_65_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P65-0'].edges.findAt (coordinates = ((5.545918928706041,0,15.721403289391581), (5.546118928706041,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_65_up_M'], name='Constraint-65_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_65_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_65_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-29'].edges.findAt (coordinates = ((5.545918928706041,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_65_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P65-0'].edges.findAt (coordinates = ((5.545918928706041,0,17.75770757121483), (5.546118928706041,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_65_low_M'], name='Constraint-65_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_65_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_66_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-29'].edges.findAt (coordinates = ((5.553876837651919,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_66_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P66-0'].edges.findAt (coordinates = ((5.553876837651919,0,20.26970757121483), (5.554076837651919,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_66_up_M'], name='Constraint-66_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_66_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_66_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-36'].edges.findAt (coordinates = ((5.553876837651919,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_66_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P66-0'].edges.findAt (coordinates = ((5.553876837651919,0,22.069707573658953), (5.554076837651919,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_66_low_M'], name='Constraint-66_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_66_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_67_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-36'].edges.findAt (coordinates = ((5.545740246444179,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_67_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P67-0'].edges.findAt (coordinates = ((5.545740246444179,0,24.581707573658953), (5.545940246444179,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_67_up_M'], name='Constraint-67_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_67_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_67_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-43'].edges.findAt (coordinates = ((5.545740246444179,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_67_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P67-0'].edges.findAt (coordinates = ((5.545740246444179,0,26.52894336852209), (5.545940246444179,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_67_low_M'], name='Constraint-67_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_67_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_68_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-43'].edges.findAt (coordinates = ((5.546057265673858,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_68_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P68-0'].edges.findAt (coordinates = ((5.546057265673858,0,29.04094336852209), (5.546257265673858,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_68_up_M'], name='Constraint-68_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_68_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_68_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-50'].edges.findAt (coordinates = ((5.546057265673858,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_68_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P68-0'].edges.findAt (coordinates = ((5.546057265673858,0,30.922748329004936), (5.546257265673858,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_68_low_M'], name='Constraint-68_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_68_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_69_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-50'].edges.findAt (coordinates = ((5.5548958481994815,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_69_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P69-0'].edges.findAt (coordinates = ((5.5548958481994815,0,33.43474832900493), (5.555095848199481,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_69_up_M'], name='Constraint-69_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_69_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_69_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-57'].edges.findAt (coordinates = ((5.5548958481994815,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_69_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P69-0'].edges.findAt (coordinates = ((5.5548958481994815,0,35.23968964593179), (5.555095848199481,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_69_low_M'], name='Constraint-69_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_69_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_70_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-2'].edges.findAt (coordinates = ((10.092858005881162,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_70_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P70-0'].edges.findAt (coordinates = ((10.092858005881162,0,2.456), (10.093058005881161,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_70_up_M'], name='Constraint-70_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_70_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_70_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-9'].edges.findAt (coordinates = ((10.092858005881162,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_70_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P70-0'].edges.findAt (coordinates = ((10.092858005881162,0,4.353843525636163), (10.093058005881161,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_70_low_M'], name='Constraint-70_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_70_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_71_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-9'].edges.findAt (coordinates = ((10.098798547339227,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_71_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P71-0'].edges.findAt (coordinates = ((10.098798547339227,0,6.865843525636163), (10.098998547339226,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_71_up_M'], name='Constraint-71_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_71_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_71_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-16'].edges.findAt (coordinates = ((10.098798547339227,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_71_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P71-0'].edges.findAt (coordinates = ((10.098798547339227,0,8.786115177501584), (10.098998547339226,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_71_low_M'], name='Constraint-71_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_71_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_72_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-16'].edges.findAt (coordinates = ((10.098115010242106,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_72_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P72-0'].edges.findAt (coordinates = ((10.098115010242106,0,11.298115177501584), (10.098315010242105,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_72_up_M'], name='Constraint-72_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_72_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_72_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-23'].edges.findAt (coordinates = ((10.098115010242106,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_72_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P72-0'].edges.findAt (coordinates = ((10.098115010242106,0,13.209403289391583), (10.098315010242105,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_72_low_M'], name='Constraint-72_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_72_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_73_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-23'].edges.findAt (coordinates = ((10.093073132936855,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_73_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P73-0'].edges.findAt (coordinates = ((10.093073132936855,0,15.721403289391581), (10.093273132936854,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_73_up_M'], name='Constraint-73_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_73_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_73_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-30'].edges.findAt (coordinates = ((10.093073132936855,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_73_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P73-0'].edges.findAt (coordinates = ((10.093073132936855,0,17.75770757121483), (10.093273132936854,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_73_low_M'], name='Constraint-73_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_73_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_74_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-30'].edges.findAt (coordinates = ((10.092858005881162,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_74_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P74-0'].edges.findAt (coordinates = ((10.092858005881162,0,20.26970757121483), (10.093058005881161,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_74_up_M'], name='Constraint-74_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_74_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_74_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-37'].edges.findAt (coordinates = ((10.092858005881162,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_74_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P74-0'].edges.findAt (coordinates = ((10.092858005881162,0,22.069707573658953), (10.093058005881161,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_74_low_M'], name='Constraint-74_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_74_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_75_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-37'].edges.findAt (coordinates = ((10.102858005881162,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_75_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P75-0'].edges.findAt (coordinates = ((10.102858005881162,0,24.581707573658953), (10.103058005881161,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_75_up_M'], name='Constraint-75_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_75_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_75_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-44'].edges.findAt (coordinates = ((10.102858005881162,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_75_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P75-0'].edges.findAt (coordinates = ((10.102858005881162,0,26.52894336852209), (10.103058005881161,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_75_low_M'], name='Constraint-75_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_75_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_76_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-44'].edges.findAt (coordinates = ((10.098157706019439,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_76_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P76-0'].edges.findAt (coordinates = ((10.098157706019439,0,29.04094336852209), (10.098357706019438,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_76_up_M'], name='Constraint-76_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_76_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_76_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-51'].edges.findAt (coordinates = ((10.098157706019439,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_76_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P76-0'].edges.findAt (coordinates = ((10.098157706019439,0,30.922748329004936), (10.098357706019438,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_76_low_M'], name='Constraint-76_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_76_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_77_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-51'].edges.findAt (coordinates = ((10.09386158562185,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_77_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P77-0'].edges.findAt (coordinates = ((10.09386158562185,0,33.43474832900493), (10.09406158562185,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_77_up_M'], name='Constraint-77_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_77_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_77_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-58'].edges.findAt (coordinates = ((10.09386158562185,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_77_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P77-0'].edges.findAt (coordinates = ((10.09386158562185,0,35.23968964593179), (10.09406158562185,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_77_low_M'], name='Constraint-77_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_77_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_78_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-3'].edges.findAt (coordinates = ((14.54463035395753,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_78_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P78-0'].edges.findAt (coordinates = ((14.54463035395753,0,2.456), (14.54483035395753,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_78_up_M'], name='Constraint-78_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_78_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_78_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-10'].edges.findAt (coordinates = ((14.54463035395753,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_78_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P78-0'].edges.findAt (coordinates = ((14.54463035395753,0,4.353843525636163), (14.54483035395753,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_78_low_M'], name='Constraint-78_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_78_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_79_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-10'].edges.findAt (coordinates = ((14.5477115463007,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_79_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P79-0'].edges.findAt (coordinates = ((14.5477115463007,0,6.865843525636163), (14.5479115463007,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_79_up_M'], name='Constraint-79_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_79_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_79_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-17'].edges.findAt (coordinates = ((14.5477115463007,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_79_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P79-0'].edges.findAt (coordinates = ((14.5477115463007,0,8.786115177501584), (14.5479115463007,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_79_low_M'], name='Constraint-79_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_79_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_80_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-17'].edges.findAt (coordinates = ((14.541704768921075,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_80_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P80-0'].edges.findAt (coordinates = ((14.541704768921075,0,11.298115177501584), (14.541904768921075,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_80_up_M'], name='Constraint-80_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_80_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_80_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-24'].edges.findAt (coordinates = ((14.541704768921075,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_80_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P80-0'].edges.findAt (coordinates = ((14.541704768921075,0,13.209403289391583), (14.541904768921075,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_80_low_M'], name='Constraint-80_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_80_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_81_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-24'].edges.findAt (coordinates = ((14.551464855279448,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_81_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P81-0'].edges.findAt (coordinates = ((14.551464855279448,0,15.721403289391581), (14.551664855279448,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_81_up_M'], name='Constraint-81_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_81_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_81_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-31'].edges.findAt (coordinates = ((14.551464855279448,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_81_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P81-0'].edges.findAt (coordinates = ((14.551464855279448,0,17.75770757121483), (14.551664855279448,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_81_low_M'], name='Constraint-81_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_81_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_82_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-31'].edges.findAt (coordinates = ((14.550930419235131,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_82_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P82-0'].edges.findAt (coordinates = ((14.550930419235131,0,20.26970757121483), (14.55113041923513,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_82_up_M'], name='Constraint-82_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_82_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_82_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-38'].edges.findAt (coordinates = ((14.550930419235131,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_82_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P82-0'].edges.findAt (coordinates = ((14.550930419235131,0,22.069707573658953), (14.55113041923513,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_82_low_M'], name='Constraint-82_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_82_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_83_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-38'].edges.findAt (coordinates = ((14.542952936915984,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_83_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P83-0'].edges.findAt (coordinates = ((14.542952936915984,0,24.581707573658953), (14.543152936915984,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_83_up_M'], name='Constraint-83_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_83_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_83_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-45'].edges.findAt (coordinates = ((14.542952936915984,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_83_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P83-0'].edges.findAt (coordinates = ((14.542952936915984,0,26.52894336852209), (14.543152936915984,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_83_low_M'], name='Constraint-83_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_83_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_84_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-45'].edges.findAt (coordinates = ((14.548419557536766,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_84_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P84-0'].edges.findAt (coordinates = ((14.548419557536766,0,29.04094336852209), (14.548619557536766,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_84_up_M'], name='Constraint-84_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_84_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_84_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-52'].edges.findAt (coordinates = ((14.548419557536766,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_84_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P84-0'].edges.findAt (coordinates = ((14.548419557536766,0,30.922748329004936), (14.548619557536766,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_84_low_M'], name='Constraint-84_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_84_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_85_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-52'].edges.findAt (coordinates = ((14.542858238288305,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_85_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P85-0'].edges.findAt (coordinates = ((14.542858238288305,0,33.43474832900493), (14.543058238288305,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_85_up_M'], name='Constraint-85_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_85_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_85_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-59'].edges.findAt (coordinates = ((14.542858238288305,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_85_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P85-0'].edges.findAt (coordinates = ((14.542858238288305,0,35.23968964593179), (14.543058238288305,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_85_low_M'], name='Constraint-85_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_85_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_86_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-4'].edges.findAt (coordinates = ((19.045784021694324,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_86_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P86-0'].edges.findAt (coordinates = ((19.045784021694324,0,2.456), (19.045984021694323,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_86_up_M'], name='Constraint-86_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_86_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_86_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-11'].edges.findAt (coordinates = ((19.045784021694324,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_86_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P86-0'].edges.findAt (coordinates = ((19.045784021694324,0,4.353843525636163), (19.045984021694323,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_86_low_M'], name='Constraint-86_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_86_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_87_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-11'].edges.findAt (coordinates = ((19.049488801278653,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_87_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P87-0'].edges.findAt (coordinates = ((19.049488801278653,0,6.865843525636163), (19.049688801278652,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_87_up_M'], name='Constraint-87_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_87_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_87_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-18'].edges.findAt (coordinates = ((19.049488801278653,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_87_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P87-0'].edges.findAt (coordinates = ((19.049488801278653,0,8.786115177501584), (19.049688801278652,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_87_low_M'], name='Constraint-87_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_87_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_88_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-18'].edges.findAt (coordinates = ((19.054594320583323,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_88_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P88-0'].edges.findAt (coordinates = ((19.054594320583323,0,11.298115177501584), (19.054794320583323,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_88_up_M'], name='Constraint-88_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_88_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_88_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-25'].edges.findAt (coordinates = ((19.054594320583323,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_88_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P88-0'].edges.findAt (coordinates = ((19.054594320583323,0,13.209403289391583), (19.054794320583323,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_88_low_M'], name='Constraint-88_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_88_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_89_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-25'].edges.findAt (coordinates = ((19.045762412528827,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_89_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P89-0'].edges.findAt (coordinates = ((19.045762412528827,0,15.721403289391581), (19.045962412528826,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_89_up_M'], name='Constraint-89_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_89_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_89_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-32'].edges.findAt (coordinates = ((19.045762412528827,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_89_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P89-0'].edges.findAt (coordinates = ((19.045762412528827,0,17.75770757121483), (19.045962412528826,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_89_low_M'], name='Constraint-89_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_89_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_90_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-32'].edges.findAt (coordinates = ((19.046438475529456,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_90_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P90-0'].edges.findAt (coordinates = ((19.046438475529456,0,20.26970757121483), (19.046638475529456,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_90_up_M'], name='Constraint-90_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_90_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_90_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-39'].edges.findAt (coordinates = ((19.046438475529456,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_90_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P90-0'].edges.findAt (coordinates = ((19.046438475529456,0,22.069707573658953), (19.046638475529456,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_90_low_M'], name='Constraint-90_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_90_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_91_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-39'].edges.findAt (coordinates = ((19.048200878952024,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_91_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P91-0'].edges.findAt (coordinates = ((19.048200878952024,0,24.581707573658953), (19.048400878952023,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_91_up_M'], name='Constraint-91_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_91_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_91_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-46'].edges.findAt (coordinates = ((19.048200878952024,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_91_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P91-0'].edges.findAt (coordinates = ((19.048200878952024,0,26.52894336852209), (19.048400878952023,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_91_low_M'], name='Constraint-91_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_91_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_92_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-46'].edges.findAt (coordinates = ((19.05219479822734,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_92_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P92-0'].edges.findAt (coordinates = ((19.05219479822734,0,29.04094336852209), (19.05239479822734,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_92_up_M'], name='Constraint-92_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_92_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_92_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-53'].edges.findAt (coordinates = ((19.05219479822734,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_92_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P92-0'].edges.findAt (coordinates = ((19.05219479822734,0,30.922748329004936), (19.05239479822734,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_92_low_M'], name='Constraint-92_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_92_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_93_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-53'].edges.findAt (coordinates = ((19.046504641117814,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_93_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P93-0'].edges.findAt (coordinates = ((19.046504641117814,0,33.43474832900493), (19.046704641117813,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_93_up_M'], name='Constraint-93_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_93_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_93_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-60'].edges.findAt (coordinates = ((19.046504641117814,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_93_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P93-0'].edges.findAt (coordinates = ((19.046504641117814,0,35.23968964593179), (19.046704641117813,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_93_low_M'], name='Constraint-93_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_93_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_94_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-5'].edges.findAt (coordinates = ((23.36776243237677,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_94_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P94-0'].edges.findAt (coordinates = ((23.36776243237677,0,2.456), (23.36796243237677,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_94_up_M'], name='Constraint-94_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_94_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_94_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-12'].edges.findAt (coordinates = ((23.36776243237677,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_94_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P94-0'].edges.findAt (coordinates = ((23.36776243237677,0,4.353843525636163), (23.36796243237677,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_94_low_M'], name='Constraint-94_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_94_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_95_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-12'].edges.findAt (coordinates = ((23.358562156174994,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_95_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P95-0'].edges.findAt (coordinates = ((23.358562156174994,0,6.865843525636163), (23.358762156174993,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_95_up_M'], name='Constraint-95_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_95_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_95_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-19'].edges.findAt (coordinates = ((23.358562156174994,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_95_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P95-0'].edges.findAt (coordinates = ((23.358562156174994,0,8.786115177501584), (23.358762156174993,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_95_low_M'], name='Constraint-95_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_95_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_96_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-19'].edges.findAt (coordinates = ((23.358577038868106,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_96_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P96-0'].edges.findAt (coordinates = ((23.358577038868106,0,11.298115177501584), (23.358777038868105,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_96_up_M'], name='Constraint-96_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_96_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_96_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-26'].edges.findAt (coordinates = ((23.358577038868106,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_96_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P96-0'].edges.findAt (coordinates = ((23.358577038868106,0,13.209403289391583), (23.358777038868105,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_96_low_M'], name='Constraint-96_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_96_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_97_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-26'].edges.findAt (coordinates = ((23.36303626282881,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_97_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P97-0'].edges.findAt (coordinates = ((23.36303626282881,0,15.721403289391581), (23.36323626282881,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_97_up_M'], name='Constraint-97_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_97_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_97_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-33'].edges.findAt (coordinates = ((23.36303626282881,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_97_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P97-0'].edges.findAt (coordinates = ((23.36303626282881,0,17.75770757121483), (23.36323626282881,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_97_low_M'], name='Constraint-97_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_97_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_98_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-33'].edges.findAt (coordinates = ((23.358293915336166,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_98_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P98-0'].edges.findAt (coordinates = ((23.358293915336166,0,20.26970757121483), (23.358493915336165,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_98_up_M'], name='Constraint-98_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_98_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_98_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-40'].edges.findAt (coordinates = ((23.358293915336166,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_98_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P98-0'].edges.findAt (coordinates = ((23.358293915336166,0,22.069707573658953), (23.358493915336165,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_98_low_M'], name='Constraint-98_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_98_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_99_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-40'].edges.findAt (coordinates = ((23.35858588386132,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_99_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P99-0'].edges.findAt (coordinates = ((23.35858588386132,0,24.581707573658953), (23.35878588386132,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_99_up_M'], name='Constraint-99_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_99_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_99_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-47'].edges.findAt (coordinates = ((23.35858588386132,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_99_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P99-0'].edges.findAt (coordinates = ((23.35858588386132,0,26.52894336852209), (23.35878588386132,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_99_low_M'], name='Constraint-99_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_99_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_100_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-47'].edges.findAt (coordinates = ((23.35776243237677,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_100_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P100-0'].edges.findAt (coordinates = ((23.35776243237677,0,29.04094336852209), (23.35796243237677,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_100_up_M'], name='Constraint-100_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_100_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_100_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-54'].edges.findAt (coordinates = ((23.35776243237677,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_100_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P100-0'].edges.findAt (coordinates = ((23.35776243237677,0,30.922748329004936), (23.35796243237677,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_100_low_M'], name='Constraint-100_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_100_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_101_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-54'].edges.findAt (coordinates = ((23.362461686691717,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_101_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P101-0'].edges.findAt (coordinates = ((23.362461686691717,0,33.43474832900493), (23.362661686691716,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_101_up_M'], name='Constraint-101_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_101_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_101_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-61'].edges.findAt (coordinates = ((23.362461686691717,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_101_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P101-0'].edges.findAt (coordinates = ((23.362461686691717,0,35.23968964593179), (23.362661686691716,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_101_low_M'], name='Constraint-101_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_101_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_102_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-6'].edges.findAt (coordinates = ((27.840122856090023,0,2.456),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_102_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P102-0'].edges.findAt (coordinates = ((27.840122856090023,0,2.456), (27.840322856090022,0,2.456),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_102_up_M'], name='Constraint-102_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_102_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_102_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-13'].edges.findAt (coordinates = ((27.840122856090023,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_102_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P102-0'].edges.findAt (coordinates = ((27.840122856090023,0,4.353843525636163), (27.840322856090022,0,4.353843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_102_low_M'], name='Constraint-102_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_102_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_103_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-13'].edges.findAt (coordinates = ((27.840348080090347,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_103_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P103-0'].edges.findAt (coordinates = ((27.840348080090347,0,6.865843525636163), (27.840548080090347,0,6.865843525636163),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_103_up_M'], name='Constraint-103_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_103_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_103_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-20'].edges.findAt (coordinates = ((27.840348080090347,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_103_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P103-0'].edges.findAt (coordinates = ((27.840348080090347,0,8.786115177501584), (27.840548080090347,0,8.786115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_103_low_M'], name='Constraint-103_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_103_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_104_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-20'].edges.findAt (coordinates = ((27.840122856090023,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_104_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P104-0'].edges.findAt (coordinates = ((27.840122856090023,0,11.298115177501584), (27.840322856090022,0,11.298115177501584),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_104_up_M'], name='Constraint-104_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_104_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_104_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-27'].edges.findAt (coordinates = ((27.840122856090023,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_104_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P104-0'].edges.findAt (coordinates = ((27.840122856090023,0,13.209403289391583), (27.840322856090022,0,13.209403289391583),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_104_low_M'], name='Constraint-104_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_104_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_105_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-27'].edges.findAt (coordinates = ((27.841238305508966,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_105_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P105-0'].edges.findAt (coordinates = ((27.841238305508966,0,15.721403289391581), (27.841438305508966,0,15.721403289391581),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_105_up_M'], name='Constraint-105_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_105_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_105_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-34'].edges.findAt (coordinates = ((27.841238305508966,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_105_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P105-0'].edges.findAt (coordinates = ((27.841238305508966,0,17.75770757121483), (27.841438305508966,0,17.75770757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_105_low_M'], name='Constraint-105_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_105_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_106_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-34'].edges.findAt (coordinates = ((27.842047148391266,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_106_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P106-0'].edges.findAt (coordinates = ((27.842047148391266,0,20.26970757121483), (27.842247148391266,0,20.26970757121483),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_106_up_M'], name='Constraint-106_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_106_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_106_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-41'].edges.findAt (coordinates = ((27.842047148391266,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_106_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P106-0'].edges.findAt (coordinates = ((27.842047148391266,0,22.069707573658953), (27.842247148391266,0,22.069707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_106_low_M'], name='Constraint-106_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_106_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_107_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-41'].edges.findAt (coordinates = ((27.841009900360223,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_107_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P107-0'].edges.findAt (coordinates = ((27.841009900360223,0,24.581707573658953), (27.841209900360223,0,24.581707573658953),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_107_up_M'], name='Constraint-107_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_107_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_107_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-48'].edges.findAt (coordinates = ((27.841009900360223,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_107_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P107-0'].edges.findAt (coordinates = ((27.841009900360223,0,26.52894336852209), (27.841209900360223,0,26.52894336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_107_low_M'], name='Constraint-107_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_107_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_108_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-48'].edges.findAt (coordinates = ((27.842116266212162,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_108_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P108-0'].edges.findAt (coordinates = ((27.842116266212162,0,29.04094336852209), (27.842316266212162,0,29.04094336852209),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_108_up_M'], name='Constraint-108_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_108_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_108_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-55'].edges.findAt (coordinates = ((27.842116266212162,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_108_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P108-0'].edges.findAt (coordinates = ((27.842116266212162,0,30.922748329004936), (27.842316266212162,0,30.922748329004936),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_108_low_M'], name='Constraint-108_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_108_low_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_109_up_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-55'].edges.findAt (coordinates = ((27.844937698931577,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_109_up_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P109-0'].edges.findAt (coordinates = ((27.844937698931577,0,33.43474832900493), (27.845137698931577,0,33.43474832900493),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_109_up_M'], name='Constraint-109_up', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_109_up_S'],thickness=ON, tieRotations=ON)
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_109_low_M',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['NodeOnly-62'].edges.findAt (coordinates = ((27.844937698931577,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].rootAssembly.Surface(name='serp_109_low_S',side1Edges=mdb.models['Onerow_Stretch'].rootAssembly.instances['P109-0'].edges.findAt (coordinates = ((27.844937698931577,0,35.23968964593179), (27.845137698931577,0,35.23968964593179),)))
mdb.models['Onerow_Stretch'].Tie(adjust=ON, master=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_109_low_M'], name='Constraint-109_low', positionToleranceMethod=COMPUTED, slave=mdb.models['Onerow_Stretch'].rootAssembly.surfaces['serp_109_low_S'],thickness=ON, tieRotations=ON)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P0.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P1.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P10.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P100.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P101.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P102.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P103.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P104.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P105.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P106.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P107.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P108.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P109.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P11.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P12.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P13.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P14.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P15.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P16.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P17.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P18.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P19.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P2.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P20.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P21.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P22.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P23.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P24.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P25.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P26.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P27.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P28.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P29.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P3.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P30.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P31.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P32.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P33.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P34.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P35.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P36.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P37.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P38.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P39.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P4.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P40.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P41.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P42.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P43.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P44.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P45.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P46.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P47.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P48.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P49.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P5.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P50.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P51.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P52.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P53.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P54.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P55.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P56.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P57.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P58.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P59.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P6.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P60.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P61.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P62.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P63.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P64.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P65.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P66.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P67.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P68.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P69.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P7.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P70.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P71.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P72.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P73.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P74.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P75.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P76.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P77.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P78.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P79.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P8.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P80.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P81.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P82.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P83.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P84.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P85.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P86.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P87.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P88.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P89.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P9.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P90.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P91.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P92.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P93.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P94.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P95.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P96.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P97.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P98.py',__main__.__dict__)
execfile('c:\Users\Tanay\OneDrive - Leland Stanford Junior University\Research_Personal\Mar19_HemisphereDip\\7.2_OptimusAbaqusOpt\\6_generateAbaqusAssembly\meshingScripts\P99.py',__main__.__dict__)
