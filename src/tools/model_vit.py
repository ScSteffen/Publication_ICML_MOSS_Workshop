# %%
import torch
from torchvision.models import vit_b_16, ViT_B_16_Weights
from transformers import ViTForImageClassification

def vit_b32(n_classes=10):
    """
    Load a pre-trained Vision Transformer (ViT) model for image classification
    and configure it for a specific number of classes.

    Parameters:
    - n_classes (int): Number of classes for the classification task. Default is 10.

    Returns:
    - model (torch.nn.Module): Configured ViT model for image classification.
    """
    # === pytorch version =====
    # Load the pre-trained ViT model with the specified configuration
    #weights = ViT_B_16_Weights.DEFAULT  # Use the default pre-trained weights
    #model = vit_b_16(weights=weights)
    #
    ## Modify the classifier head to match the number of output classes
    #model.heads.head = torch.nn.Linear(model.heads.head.in_features, n_classes)

    # ==== transformers version 
    model = ViTForImageClassification.from_pretrained(
        "google/vit-base-patch16-224",
        torch_dtype=torch.float32,
        num_labels=n_classes,
        ignore_mismatched_sizes=True,
    )
    return model

