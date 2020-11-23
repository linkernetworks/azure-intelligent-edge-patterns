import React, { useState, useCallback, useRef } from 'react';
import {
  Panel,
  TextField,
  Stack,
  PrimaryButton,
  DefaultButton,
  ProgressIndicator,
  Toggle,
  IIconProps,
  Label,
} from '@fluentui/react';
import * as R from 'ramda';
import { useDispatch } from 'react-redux';

export enum PanelMode {
  Create,
  Update,
}

type AddModelPanelProps = {
  isOpen: boolean;
  initialValue?: Form;
  mode: PanelMode;
  onDissmiss: () => void;
};

type FormData<V> = {
  value: V;
  errMsg: string;
};

type Form = {
  modelName: FormData<string>;
  endPoint: FormData<string>;
  key: string;
  header: string;
  secure: boolean;
};

const initialForm: Form = {
  modelName: { value: '', errMsg: '' },
  endPoint: { value: '', errMsg: '' },
  key: '',
  header: '',
  secure: false,
};

const uploadIcon: IIconProps = { iconName: 'Upload' };

const AddModelPanel: React.FC<AddModelPanelProps> = ({
  isOpen,
  initialValue = initialForm,
  mode,
  onDissmiss,
}) => {
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState<Form>(initialValue);

  const fileInputRef = useRef(null);

  const dispatch = useDispatch();

  const validate = useCallback(() => {
    let hasError = false;

    ['modelName', 'endPoint'].forEach((key) => {
      if (!formData[key].value) {
        setFormData(R.assocPath([key, 'errMsg'], `This field is required`));
        hasError = true;
      }
    });

    return hasError;
  }, [formData]);

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>): void => {
    console.log(e.target.files);
  };

  const onConfirm = useCallback(async () => {
    if (validate()) return;

    setLoading(true);
    // console.log('formData', formData);
    alert('Coming soon');
    setLoading(false);
    onDissmiss();
  }, [dispatch, formData.modelName.value, formData.endPoint.value, mode, onDissmiss, validate]);

  const onRenderFooterContent = useCallback(
    () => (
      <Stack tokens={{ childrenGap: 5 }} horizontal>
        <PrimaryButton onClick={onConfirm} disabled={loading}>
          {mode === PanelMode.Create ? 'Add' : 'Update'}
        </PrimaryButton>
        <DefaultButton onClick={onDissmiss}>Cancel</DefaultButton>
      </Stack>
    ),
    [loading, mode, onConfirm, onDissmiss],
  );

  const onChange = (key: string) => (_, newValue) => {
    setFormData(R.assocPath([key, 'value'], newValue));
  };

  const handleToggle = () => {
    setFormData({ ...formData, secure: !formData.secure });
  };

  return (
    <Panel
      isOpen={isOpen}
      onDismiss={onDissmiss}
      hasCloseButton
      headerText="Add Model"
      onRenderFooterContent={onRenderFooterContent}
      isFooterAtBottom={true}
    >
      <ProgressIndicator progressHidden={!loading} />
      <TextField
        label="Model name"
        value={formData.modelName.value}
        errorMessage={formData.modelName.errMsg}
        onChange={onChange('modelName')}
        required
      />
      <TextField
        label="Endpoint"
        value={formData.endPoint.value}
        errorMessage={formData.endPoint.errMsg}
        onChange={onChange('endPoint')}
      />
      <Stack styles={{ root: { padding: '5px 0', display: 'block' } }}>
        <Label>Labels</Label>
        <DefaultButton text="Upload" iconProps={uploadIcon} label="Labels" onClick={handleUploadClick} />
        <input
          ref={fileInputRef}
          type="file"
          onChange={handleUpload}
          // accept="image/*"
          // multiple
          style={{ display: 'none' }}
        />
      </Stack>
      <TextField label="Key" value={formData.key} errorMessage={formData.key} onChange={onChange('key')} />
      <Toggle label="Secure" checked={formData.secure} onText="On" offText="Off" onChange={handleToggle} />
      <TextField label="Header" value={formData.header} onChange={onChange('header')} />
    </Panel>
  );
};

export default AddModelPanel;
