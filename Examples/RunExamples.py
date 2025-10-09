#import individual examples
from IMAP import AppendMessageToFolder,BuildingComplexQueries,CaseSensitiveEmailsFiltering,CopyMessageToAnotherFolder,DeleteMultipleMessages,DeleteSingleMessage
from IMAP import FetchEmailMessageFromServer,FilteringMessagesFromIMAPMailbox,GetMessagesWithSpecificCriterion,GettingFoldersInformation,ListingMessagesRecursively
from IMAP import ListingMessagesWithPagingSupport,ListingMIMEMessageIdInImapMessageInfo,MoveMessageToAnotherFolder,RetrievingServerExtensions,SavingMessageFromIMAPServer
from IMAP import SetCustomFlags,SettingMessageFlags,SSLEnabledIMAPServer
from POP3 import ConnectingToPOP3,DeleteEmailByIndex,FilterMessagesFromMailbox,GetEmailCountInMailbox,GettingMailboxInfo,ListingServerExtensions,RetrieveMessageSummaryInformationUsingUniqueId
from POP3 import RetrievingEmailHeaders,RetrievingEmailMessages,SaveToDiscWithoutParsing,SSLEnabledPOP3Server
from SMTP import ForwardEmail,RetrieveSMTPServerExtensions,SendEmailSynchronously,SendingBulkEmails,SendingMeetingRequestsViaEmail,SendingPlainTextMessage,SendMsgAsTNEF
from SMTP import SetAlternateText,SettingHTMLBody,SSLEnabledSMTPServer
from Thunderbird import CreateNewMessagesToThunderbird,GetCurrentMessageSize,GetNumberOfItemsFromMBox,ReadMessagesFromThunderbird
from WorkingWithAppointments import CreateAppointment,DraftAppointmentRequest,LoadAppointment,ReadMultipleEventsFromICS,SetParticipantStatusOfAppointmentAttendees,WriteMultipleEventsToICS

from WorkingWithMimeMessages import AddEmailAttachments,ChangeEmailAddress,ConvertToMHTMLWithoutInlineImages,CreateNewMailMesssage,DetectDifferentFileFormats,DetermineAttachmendEmbeddedMessage
from WorkingWithMimeMessages import DisplayAttachmentFileName,DisplayEmailInformation,ExtractEmbeddedObjectsFromEmail,ExtractingEmailHeaders,GetDecodedHeaderValues,LoadMessageWithLoadOptions
from WorkingWithMimeMessages import MailMessageFeatures,PreserveEmbeddedMSGFormatDuringLoad,PreserveOriginalBoundaries,PreserveTnefAttachment,ReadMessageByPreservingTNEFAttachments,RemoveLRTracesFromMessageBody
from WorkingWithMimeMessages import RemovingAttachmentFromMailMessage,RequestReadReceipt,RetrievContentDescriptionFromAttachment,SaveMailMessageAsMHTML,SaveMessageAsHTML,SaveMessageAsOFT
from WorkingWithMimeMessages import SavingMSGWithPreservedDates,SetEmailHeaders,SpecifyCustomHeader,SpecifyRecipientAddresses

from WorkingWithOutlookMSGs import AddAudioReminderToCalendar,AddDisplayReminderToCalendar,AddingMSGAttachments,AddRecurrenceToMapiTask,AddReminderInformationToMapiTask,ConvertMSGToMimeMessage
from WorkingWithOutlookMSGs import CreateAndSaveCalendarItems,CreateAndSaveOutlookContact,CreateAndSaveOutlookNote,CreatingAndSavingOutlookMSG,CreatingAndSavingOutlookTask,CreatingMSGFilesWithRtfBody
from WorkingWithOutlookMSGs import DisplayReceipientsStatusFromMeetingReqeust,GetAttachmentsFromCalendar,GetMapiProperty,LoadingContactFromMSG,LoadingContactFromVCardWithSpecifiedEncoding
from WorkingWithOutlookMSGs import LoadingContactFromVCF,LoadMsgFiles,PreservingEmbeddedMsgFormat,ReadingMapiNote,ReadingOnlyVotingButtons,ReadingVotingOptions
from WorkingWithOutlookMSGs import RenderingContactInformationToMhtml,SaveMSGAsTemplate,SavingMessageInDraftStatus,SetBodyCompression,SetMapiProperties

from WorkingWithOutlookStorageFiles import AddFilesToPST,AddMapiCalendarToPST,AddMapiNoteToPST,AddMapiTaskToPST,AddMessagesFromOtherPST,AddMessagesToPSTFiles,ChangeFolderContainerClass
from WorkingWithOutlookStorageFiles import ConvertingOSTToPST,CreateDistributionListInPST,CreateNewMapiContactsAndAddToContactsSubFolder,CreateNewMapiJournalAndAddToPST,CreateNewPSTFileAndAddingSubfolders
from WorkingWithOutlookStorageFiles import DeleteBulkItemsFromPst,DeleteMessagesFromPSTFile,DisplayInformationOfPSTFile,ExtractNumberOfMessages,GetMessagesInformation,MoveItemsToOtherFolders
from WorkingWithOutlookStorageFiles import ReadingOSTFiles,RetrievingParentFolderInformationFromMessageInfo,SearchingStringInPSTWithIgnoreCaseParameter,UpdateBulkMessagesInPSTFile

###################################
#Uncomment any of the following for testing
###################################

###### IMAP
#AppendMessageToFolder.run()
#BuildingComplexQueries.run()
#CaseSensitiveEmailsFiltering.run()
#CopyMessageToAnotherFolder.run()
#DeleteMultipleMessages.run()
#DeleteSingleMessage.run()
#FetchEmailMessageFromServer.run()
#FilteringMessagesFromIMAPMailbox.run()
#GetMessagesWithSpecificCriterion.run()
#GettingFoldersInformation.run()
#ListingMessagesRecursively.run()
#ListingMessagesWithPagingSupport.run()
#ListingMIMEMessageIdInImapMessageInfo.run()
#MoveMessageToAnotherFolder.run()
#RetrievingServerExtensions.run()
#SavingMessageFromIMAPServer.run()
#SetCustomFlags.run()
#SettingMessageFlags.run()
#SSLEnabledIMAPServer.run()

###### POP3
#ConnectingToPOP3.run()
##DeleteEmailByIndex.run()
#FilterMessagesFromMailbox.run()
#GetEmailCountInMailbox.run()
#GettingMailboxInfo.run()
#ListingServerExtensions.run()
#RetrieveMessageSummaryInformationUsingUniqueId.run()
#RetrievingEmailHeaders.run()
#RetrievingEmailMessages.run()
#SaveToDiscWithoutParsing.run()
#SSLEnabledPOP3Server.run()

###### SMTP 
#ForwardEmail.run()
#RetrieveSMTPServerExtensions.run()
#SendEmailSynchronously.run()
#SendingBulkEmails.run()
#SendingMeetingRequestsViaEmail.run()
#SendingPlainTextMessage.run()
#SendMsgAsTNEF.run()
#SetAlternateText.run()
#SettingHTMLBody.run()
#SSLEnabledSMTPServer.run()

###### Thunderbird
#CreateNewMessagesToThunderbird.run()
#GetCurrentMessageSize.run()
#GetNumberOfItemsFromMBox.run()
#ReadMessagesFromThunderbird.run()

###### Working with Appointments
#CreateAppointment.run()
#DraftAppointmentRequest.run()
#LoadAppointment.run()
#ReadMultipleEventsFromICS.run()
#SetParticipantStatusOfAppointmentAttendees.run()
#WriteMultipleEventsToICS.run()

###### Working with MIME Messages
#AddEmailAttachments.run()
#ChangeEmailAddress.run()
#ConvertToMHTMLWithoutInlineImages.run()
#CreateNewMailMesssage.run()
#DetectDifferentFileFormats.run()
#DetermineAttachmendEmbeddedMessage.run()
#DisplayAttachmentFileName.run()
#DisplayEmailInformation.run()
#ExtractEmbeddedObjectsFromEmail.run()
#ExtractingEmailHeaders.run()
#GetDecodedHeaderValues.run()
#LoadMessageWithLoadOptions.run()
#MailMessageFeatures.run()
#PreserveEmbeddedMSGFormatDuringLoad.run()
#PreserveOriginalBoundaries.run()
#PreserveTnefAttachment.run()
#ReadMessageByPreservingTNEFAttachments.run()
#RemoveLRTracesFromMessageBody.run()
#RemovingAttachmentFromMailMessage.run()
#RetrievContentDescriptionFromAttachment.run()
#SaveMailMessageAsMHTML.run()
#SaveMessageAsHTML.run()
#SaveMessageAsOFT.run()
#SavingMSGWithPreservedDates.run()
#SetEmailHeaders.run()
#RequestReadReceipt.run()
#SpecifyCustomHeader.run()

###### Working with Outlook Messages
#AddAudioReminderToCalendar.run()
#AddDisplayReminderToCalendar.run()
#AddingMSGAttachments.run()
#AddRecurrenceToMapiTask.run()
#AddReminderInformationToMapiTask.run()
#ConvertMSGToMimeMessage.run()
#CreateAndSaveCalendarItems.run()
#CreateAndSaveOutlookContact.run()
#CreateAndSaveOutlookNote.run()
#CreatingAndSavingOutlookMSG.run()
#CreatingAndSavingOutlookTask.run()
#CreatingMSGFilesWithRtfBody.run()
#DisplayReceipientsStatusFromMeetingReqeust.run()
#GetAttachmentsFromCalendar.run()
#GetMapiProperty.run()
#LoadingContactFromMSG.run()
#LoadingContactFromVCardWithSpecifiedEncoding.run()
#LoadingContactFromVCF.run()
#LoadMsgFiles.run()
#PreservingEmbeddedMsgFormat.run()
#ReadingMapiNote.run()
#ReadingOnlyVotingButtons.run()
#ReadingVotingOptions.run()
#RenderingContactInformationToMhtml.run()
#SaveMSGAsTemplate.run()
#SavingMessageInDraftStatus.run()
#SetBodyCompression.run()
#SetMapiProperties.run()

###### Working with Outlook Storage Files
#AddFilesToPST.run()
#AddMapiCalendarToPST.run()
#AddMapiNoteToPST.run()
#AddMapiTaskToPST.run()
#AddMessagesFromOtherPST.run()
#AddMessagesToPSTFiles.run()
#ChangeFolderContainerClass.run()
#ConvertingOSTToPST.run()
#CreateDistributionListInPST.run()
#CreateNewMapiContactsAndAddToContactsSubFolder.run()
#CreateNewMapiJournalAndAddToPST.run()
#CreateNewPSTFileAndAddingSubfolders.run()
#DeleteBulkItemsFromPst.run()
#DeleteMessagesFromPSTFile.run()
#DisplayInformationOfPSTFile.run()
#ExtractNumberOfMessages.run()
#GetMessagesInformation.run()
#MoveItemsToOtherFolders.run()
#ReadingOSTFiles.run()
#RetrievingParentFolderInformationFromMessageInfo.run()
#SearchingStringInPSTWithIgnoreCaseParameter.run()
#UpdateBulkMessagesInPSTFile.run()