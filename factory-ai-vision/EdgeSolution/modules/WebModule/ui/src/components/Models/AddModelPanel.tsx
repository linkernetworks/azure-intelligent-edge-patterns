import React, { useState, useMemo, useCallback, useRef } from 'react';
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

import {} from '../../store/project/projectActions';

const toBase64 = (file) =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });

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
  name: string;
  endPoint: string;
  labels: string;
  header: string;
  setting: boolean;
};

const initialForm: Form = {
  name: '',
  endPoint: '',
  labels: '',
  header: '',
  setting: false,
};

const uploadIcon: IIconProps = { iconName: 'Upload' };

const AddModelPanel: React.FC<AddModelPanelProps> = ({
  isOpen,
  initialValue = initialForm,
  mode,
  onDissmiss,
}) => {
  const [isError, setIsError] = useState(false);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState<Form>(initialValue);

  const fileInputRef = useRef(null);

  const errMsg = useMemo(() => {
    if (isError) return `This field is required`;
    return '';
  }, [isError]);

  const dispatch = useDispatch();

  const validate = useCallback(() => {
    let hasError = false;

    ['modelName', 'endPoint'].forEach((key) => {
      if (!formData[key]) {
        hasError = true;
      }
    });

    return hasError;
  }, [formData]);

  const handleInputClick = () => {
    fileInputRef.current.click();
  };

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.files[0]);
    const file = (await toBase64(e.target.files[0])) as string;

    if (file) {
      setFormData({
        ...formData,
        labels: file,
      });
    }
  };

  const onConfirm = useCallback(async () => {
    if (validate()) {
      setIsError(true);
      return;
    }

    setLoading(true);
    console.log('formData', formData);
    alert('Coming soon');
    setLoading(false);
    // onDissmiss();
  }, [dispatch, formData.name, formData.endPoint, mode, onDissmiss, validate]);

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
    setIsError(false);

    setFormData(R.assocPath([key], newValue));
  };

  const handleSecureToggle = () => {
    setFormData({ ...formData, setting: !formData.setting });
  };

  console.log('formData', formData);

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
        value={formData.name}
        errorMessage={errMsg}
        onChange={onChange('name')}
        required
      />
      <TextField
        label="Endpoint"
        value={formData.endPoint}
        errorMessage={errMsg}
        onChange={onChange('endPoint')}
        required
      />
      <Stack styles={{ root: { padding: '5px 0', display: 'block' } }}>
        <Label>Labels</Label>
        <DefaultButton text="Upload" iconProps={uploadIcon} label="Labels" onClick={handleInputClick} />
        <input
          ref={fileInputRef}
          type="file"
          onChange={handleUpload}
          accept=".txt"
          style={{ display: 'none' }}
        />
      </Stack>
      <Toggle
        label="Secure"
        checked={formData.setting}
        onText="On"
        offText="Off"
        onChange={handleSecureToggle}
      />
      <TextField label="Header" value={formData.header} onChange={onChange('header')} />
    </Panel>
  );
};

export default AddModelPanel;
