from BluenetLib.lib.core.uart.UartTypes import UartTxType
from BluenetLib.lib.core.uart.UartWrapper import UartWrapper
from BluenetLib.lib.util.EventBus import eventBus, SystemTopics


class UsbDevHandler:
    
    def __init__(self):
        pass
    
    def setAdvertising(self, enabled):
        """
            Enable/ disable the advertising
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.ENABLE_ADVERTISEMENT, self._getPayload(enabled)).getPacket())
    
    def setMeshing(self, enabled):
        """
            Enable/ disable the Meshing
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.ENABLE_MESH, self._getPayload(enabled)).getPacket())
    
    def requestCrownstoneId(self):
        """
            Request the Crownstone ID. This is a uint16
            :return:
        """
        self._send(UartWrapper(UartTxType.GET_CROWNSTONE_ID, []).getPacket())
    
    def requestMacAddress(self):
        """
            Request the MAC address ID.
            :return:
        """
        self._send(UartWrapper(UartTxType.GET_MAC_ADDRESS, []).getPacket())
    
    def increaseCurrentRange(self):
        """
            Increase the GAIN on the current sensing
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_INC_RANGE_CURRENT, []).getPacket())
    
    def decreaseCurrentRange(self):
        """
            Decrease the GAIN on the current sensing
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_DEC_RANGE_CURRENT, []).getPacket())
    
    def increaseVoltageRange(self):
        """
            Increase the GAIN on the voltage sensing
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_INC_RANGE_VOLTAGE, []).getPacket())
    
    def decreaseVoltageRange(self):
        """
            Decrease the GAIN on the voltage sensing
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_DEC_RANGE_VOLTAGE, []).getPacket())
    
    def setDifferentialModeCurrent(self, enabled):
        """
            Enable/disable differential mode on the current sensing
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_DIFFERENTIAL_CURRENT, self._getPayload(enabled)).getPacket())
    
    def setDifferentialModeVoltage(self, enabled):
        """
            Enable/disable differential mode on the voltage sensing
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_DIFFERENTIAL_VOLTAGE, self._getPayload(enabled)).getPacket())

    def setVoltageChannelPin(self, pin):
        """
            Select the measurement pin for the voltage sensing
            :param pin: int [0 .. 255]
            :return:
        """
        self._send(UartWrapper(UartTxType.ADC_CONFIG_VOLTAGE_PIN, [pin]).getPacket())

    def setSendCurrentSamples(self, enabled):
        """
            Enable/ disable the sending of the measured current buffer.
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.POWER_LOG_CURRENT, self._getPayload(enabled)).getPacket())

    def setSendVoltageSamples(self, enabled):
        """
            Enable/ disable the sending of the measured voltage buffer.
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.POWER_LOG_VOLTAGE, self._getPayload(enabled)).getPacket())
    
    def setSendFilteredCurrentSamples(self, enabled):
        """
            Enable/ disable the sending of the filtered current sample buffer.
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.POWER_LOG_FILTERED_CURRENT, self._getPayload(enabled)).getPacket())
     
    def setSendFilteredVoltageSamples(self, enabled):
        """
            Enable/ disable the sending of the filtered voltage sample buffer.
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.POWER_LOG_FILTERED_VOLTAGE, self._getPayload(enabled)).getPacket())
    
    def setSendCalculatedSamples(self, enabled):
        """
            Enable/ disable the sending of the calculated power samples.
            :param enabled: Boolean
            :return:
        """
        self._send(UartWrapper(UartTxType.POWER_LOG_CALCULATED_POWER, self._getPayload(enabled)).getPacket())



    # MARK: internal methods
    
    def _getPayload(self, bool):
        payload = 0
        if bool:
            payload = 1
            
        return [payload]

    def _send(self, uartPacket):
        # send over uart
        eventBus.emit(SystemTopics.uartWriteData, uartPacket)
        