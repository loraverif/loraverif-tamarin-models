# Tamarin Analysis of LoRaWAN Join Protocols

This repository contains a collection of Tamarin implementations of the Join procedure for the LoRaWAN protocol suite. In addition, we include a Tamarin model of our proposed amended protocol. Our focus is on modelling the LoRaWAN OTAA Join procedure as faithfully as possible, including the modelling of counters, secure channels, and the multiple different keys given by the specification.

## Background

The LoRaWAN (Low Power, Wide Area networking) protocol suite is accepted as the de-facto standard for a range of IoT devices, designed to connect a collection of small devices to larger networks. A particular usecase is in the domain of sensor devices, who aggregate their data on a central server. The LoRaWAN 1.02 specification was finalised in July 2016, and later superceded by the 1.1 version of the specification in October 2017.

The Tamarin tool is an automated verification tool for communication protocols. It takes as input a protocol specification (written using a multiset rewriting model), as well as a set of security claims (written as a set of first order logic statements).

For further information, please refer to our paper (currently in submission).

## Layout

The files in this repository are arranged into three main folders:

- *LoRaWAN_v1_0* contains implementations of the LoRaWAN 1.02 OTAA Join protocol
- *LoRaWAN_v1_1* contains implementations of the LoRaWAN 1.1 OTAA Join protocol
- *LoRaWAN_v1_1_extended* contains implementations of our proposed LoRaWAN LoRa-3AKA+ Join protocol

Within each folder, there are a few different files. These generally refer to the different security models we consider in our paper. Each file is named `L_<version>_<model>_<sync>_<appskey>`, where:

- `<version>` represents the version of LoRa (v10, v11, vNew)
- `<model>` represents the threat model (sec, lora, corr)
- `<sync>` describes whether or not the Application Server confirms the well-formedness of message packets (sync, desync)
- `<appskey>` describes whether the Application Server receives the AppSKey from the Network Server or the Join Server, via the SessionKeyID (fromNS, fromJS)

Each folder also contains an `oracle.py` file, which is used by Tamarin to guide analysis.

## Usage

Running these models requires the Tamarin prover be installed on your system. Tamarin is supported on Mac, Linux, and Windows (using the Windows Linux Subsystem). Find more information on the [Tamarin Prover website](https://tamarin-prover.github.io/).

Each file contains a recommended command to run the analysis, using the oracle and heuristics we recommend. Each file also contains an estimated run time for Tamarin. Be aware that some of the executions can take a very long time (several hours or even a day), due to the complexity of the problem.

If you wish to run through the protocols interactively to see how they work, you can type

``` tamarin-prover interactive **path_to_file** ```

