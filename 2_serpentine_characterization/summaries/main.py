import generateSummary

if __name__ == "__main__":
  '''Create summary file for stiffness and max. lin. str relation.'''
  legList = [8]
  for leg in legList:
    print ("Processing leg: {}".format(leg))
    generateSummary.genSummary(leg, ensemble=False, forces=False)
  # generateSummary.genSummary(legList, ensemble=True)

  '''Create summary file for backdesign (arc parameters).'''
  # legList = [10]
  # for leg in legList:
  #   print ("Processing leg: {}".format(leg))
  #   generateSummary.genBackdesignSummary(leg)
  # generateSummary.genBackdesignSummary(legList, ensemble=True)
