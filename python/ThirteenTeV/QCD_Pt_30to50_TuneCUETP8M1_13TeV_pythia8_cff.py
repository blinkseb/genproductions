import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	maxEventsToPrint = cms.untracked.int32(1),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	filterEfficiency = cms.untracked.double(1.0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(13000.0),

	crossSection = cms.untracked.double(1.40932e+08),

	PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CUEP8M1SettingsBlock,
	    processParameters = cms.vstring(
			'HardQCD:all = on',
			'PhaseSpace:pTHatMin = 30  ',
			'PhaseSpace:pTHatMax = 50  ',
	    ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CUEP8M1Settings',
                                        'processParameters',
                                        )
	)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision$'),
    name = cms.untracked.string('\$Source$'),
    annotation = cms.untracked.string('QCD pthat 30to50 GeV, 13 TeV, TuneCUETP8M1')
)
