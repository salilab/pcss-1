import pcssTools
import pcssCluster
import configobj

import sys
import os


configFileName = sys.argv[1]
tempPcssConfig = configobj.ConfigObj(configFileName)
configSpec = tempPcssConfig["user_config_spec_file"]

pcssConfig = configobj.ConfigObj(configFileName, configspec=configSpec)
#pcssConfig["attribute_file_name"] = os.path.join(pcssConfig["pcss_directory"], "data", "context", "svmTrainingAttributes.txt")
runner = pcssTools.TrainingBenchmarkRunner(pcssConfig)
runner.execute()

runner = pcssTools.LeaveOneOutBenchmarkRunner(self.pcssConfig)
runner.execute()

runner = pcssTools.CompleteSvmRunner(self.pcssConfig)
runner.execute()