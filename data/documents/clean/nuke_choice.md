# nuke.choice
nuke.choice(_title_ , _prompt_ , _options_ , _default =0_)  index

Shows a dialog box with the given title and prompt text, and a combo box containing the given options.
Parameters

  * **title** – Text to put in the dialog’s title bar.
  * **prompt** – Text to display at the top of the dialog.
  * **options** – A list of strings for the user to choose from.
  * **default** – The index (starting from zero) of the option to select first.
Returns

An integer index (starting from zero) of the choice the user selected, or None if the dialog was cancelled.